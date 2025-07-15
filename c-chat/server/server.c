#include <stdio.h>      // Standard I/O: printf, perror
#include <stdlib.h>     // exit, EXIT_FAILURE
#include <string.h>     // memset (sets memory to zero)
#include <unistd.h>     // close (for cleaning up sockets)
#include <sys/types.h>  // data types for sockets
#include <sys/socket.h> // socket, bind, listen, accept
#include <netinet/in.h> // sockaddr_in struct for IPv4 addresses


#define PORT 12345
#define BUFFER_SIZE 1024

int main() {
    int server_fd;                    // File descriptor (ID) for server socket
    struct sockaddr_in server_addr;   // Struct that stores address info

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
if (server_fd < 0) { // if we have less than 0 
    perror("socket failed");
    exit(EXIT_FAILURE);
}

memset(&server_addr, 0, sizeof(server_addr));
server_addr.sin_family = AF_INET;
server_addr.sin_addr.s_addr = INADDR_ANY;
server_addr.sin_port = htons(PORT);
