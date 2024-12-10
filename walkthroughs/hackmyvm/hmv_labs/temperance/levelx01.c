#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netdb.h> // For getaddrinfo

// Define server details
#define SERVER_NAME "temperance.hackmyvm.eu" // Replace with the server's domain name
#define SERVER_PORT 9988         // Replace with the server's port

// Function to send data to the server
void send_data(int sockfd, const char *data) {
    if (write(sockfd, data, strlen(data)) < 0) {
        perror("Failed to send data to the server");
        close(sockfd);
        exit(EXIT_FAILURE);
    }
    printf("Sent to server: %s\n", data);
}

// Function to receive data from the server and optionally save it
int receive_data(int sockfd, char *output_buffer, size_t buffer_size) {
    memset(output_buffer, 0, buffer_size);
    int bytes_received = read(sockfd, output_buffer, buffer_size - 1);
    if (bytes_received < 0) {
        perror("Read failed");
        close(sockfd);
        exit(EXIT_FAILURE);
    }
    output_buffer[bytes_received] = '\0'; // Null-terminate the received string
    return bytes_received;
}

int main() {
    int sockfd;
    struct sockaddr_in server_addr;
    struct addrinfo hints, *res;

    // Resolve domain name to IP address
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_INET; // Use IPv4
    hints.ai_socktype = SOCK_STREAM; // Use TCP

    if (getaddrinfo(SERVER_NAME, NULL, &hints, &res) != 0) {
        perror("Domain name resolution failed");
        exit(EXIT_FAILURE);
    }

    // Extract IP address from the resolved address
    struct sockaddr_in *ipv4 = (struct sockaddr_in *)res->ai_addr;
    char ip_str[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &ipv4->sin_addr, ip_str, sizeof(ip_str));
    printf("Resolved %s to %s\n", SERVER_NAME, ip_str);

    // Create a socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Socket creation failed");
        freeaddrinfo(res);
        exit(EXIT_FAILURE);
    }

    // Configure server address
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(SERVER_PORT);
    server_addr.sin_addr = ipv4->sin_addr;

    // Connect to the server
    if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection to the server failed");
        freeaddrinfo(res);
        close(sockfd);
        exit(EXIT_FAILURE);
    }
    printf("Connected to the server at %s:%d\n", ip_str, SERVER_PORT);

    // Free address info after connection
    freeaddrinfo(res);

    // Step 1: Receive initial data from the server
    char initial_response[1024];
    receive_data(sockfd, initial_response, sizeof(initial_response));
    printf("Received from server: %s\n", initial_response);

    // Step 2: Send the level selection string to the server
    const char *level = "01"; // Replace with the appropriate level number
    char level_message[1024];
    snprintf(level_message, sizeof(level_message), "levelx%s", level);
    send_data(sockfd, level_message);

    // Step 3: Receive challenge data from the server and save it as "challenge"
    char challenge[1024];
    receive_data(sockfd, challenge, sizeof(challenge));
    printf("First challenge received: %s\n", challenge);

    // Step 4: Send the challenge back to the server
    send_data(sockfd, challenge);

    // Step 5: Receive the server's response and save it as "challenge_2"
    char challenge_2[1024];
    receive_data(sockfd, challenge_2, sizeof(challenge_2));
    printf("Second challenge received: %s\n", challenge_2);

    // Step 6: Send the challenge back to the server
    send_data(sockfd, challenge_2);

    // Step 7: Receive the server's response
    char final_response[1024];
    receive_data(sockfd, final_response, sizeof(final_response));
    printf("Final server response: %s\n", final_response);

    // Close the socket
    close(sockfd);
    printf("Connection closed\n");

    return 0;
}
