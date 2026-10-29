# Load Balancer Pattern

**Software Architecture course project:** Load Balancer Pattern and horizontal scaling using Nginx, Python and Docker Compose.

## 1. Project Overview

This project demonstrates the Load Balancer architectural pattern. A load balancer receives HTTP requests from clients and distributes them between multiple backend instances.

The goal is to demonstrate how a system can use more than one backend instance instead of sending all requests to a single server.

## 2. Architecture

The system contains:

- **Client:** Sends HTTP requests.
- **Nginx Load Balancer:** Receives requests and forwards them to a backend.
- **Backend 1:** A Python HTTP server.
- **Backend 2:** A second Python HTTP server.
- **Docker:** Runs the application in a container.

Nginx uses the Round Robin algorithm to distribute requests between the two backend instances.

### Architecture Diagram

```text
                 Client
                    |
                    v
          Nginx Load Balancer
             (Round Robin)
               /       \
              v         v
         Backend 1   Backend 2
           Python      Python
```

## 3. Technologies

- **Nginx:** Load balancing and reverse proxy.
- **Python:** Simple HTTP backend services.
- **Docker:** Containerization.
- **Docker Compose:** Application configuration and startup.

## 4. How It Works

1. The client sends an HTTP request to the load balancer.
2. Nginx receives the request.
3. Nginx selects a backend instance using Round Robin.
4. The selected backend processes the request.
5. The backend returns an HTTP response to the client through Nginx.

Each backend returns its own name. This makes it possible to see which instance handles each request.

## 5. How to Run the Project

Requirements: Docker and Docker Compose.

Start the application:

```bash
docker compose up --build -d
```

Send one HTTP request:

```bash
curl http://localhost:8080/
```

Send six requests to observe the distribution:

```bash
for i in {1..6}; do curl -s http://localhost:8080/; done
```

Stop the application:

```bash
docker compose down
```

## 6. Demonstration Results

The application was tested with six consecutive HTTP requests. Both backend instances returned responses through the load balancer.

Example output:

```text
Hello from Backend 2!
Hello from Backend 1!
Hello from Backend 2!
Hello from Backend 1!
Hello from Backend 2!
Hello from Backend 1!
```

This demonstrates request distribution between two backend instances.

## 7. Advantages

- Distributes requests between multiple backend instances.
- Supports horizontal scaling by adding more instances.
- Helps prevent one backend from receiving all requests.
- Makes it possible to increase application capacity.

## 8. Limitations

- The load balancer can become a single point of failure if there is only one instance.
- The backend instances must be monitored to detect failures.
- More instances require additional resources.
- Round Robin does not consider the current workload of each backend.

## 9. Conclusion

This project demonstrates the Load Balancer Pattern using Nginx, Python and Docker. The working demonstration shows how HTTP requests can be distributed between two backend instances using Round Robin.

The project provides a simple example of horizontal scaling in a distributed application.
