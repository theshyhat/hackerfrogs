<?php
// upload.php - INSECURE PDF UPLOAD DEMO (FOR LAB USE ONLY)
error_reporting(E_ALL);
ini_set('display_errors', 1);

$upload_dir = 'uploads/';
if (!file_exists($upload_dir)) {
    mkdir($upload_dir, 0777, true);
}

$message = '';
$allowed_ext = ['pdf'];

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];
    $ext = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));

    // INSECURE: Only checks file extension
    if (in_array($ext, $allowed_ext)) {
        $target_path = $upload_dir . basename($file['name']);
        
        if (move_uploaded_file($file['tmp_name'], $target_path)) {
            $message = "File uploaded! Processing with GhostScript...";
            
            // VULNERABLE GHOSTSCRIPT CALL
            shell_exec("gs -dNOPAUSE -dBATCH -sDEVICE=png16m -sOutputFile=thumb.png " . escapeshellarg($target_path));
            
            $message .= "<br>Thumbnail generated!";
        } else {
            $message = "Upload failed!";
        }
    } else {
        $message = "Only .pdf files allowed!";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>4chan-like PDF Upload</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .container { border: 1px solid #ddd; padding: 20px; border-radius: 5px; }
        .warning { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>PDF Upload Demo</h1>
        <p class="warning">WARNING: This is an INSECURE demo for educational purposes only!</p>
        
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file" accept=".pdf" required>
            <button type="submit">Upload</button>
        </form>

        <?php if (!empty($message)): ?>
            <p><?php echo $message; ?></p>
        <?php endif; ?>

        <?php if (file_exists('thumb.png')): ?>
            <h3>Generated Thumbnail:</h3>
            <img src="thumb.png" alt="Thumbnail">
        <?php endif; ?>
    </div>
</body>
</html>
