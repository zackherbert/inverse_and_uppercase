# inverse_and_uppercase

This is a small docker compose demo, made to test running containers with open ports interacting with each other.

It contains 3 containers running a python program:

 - inverse: open tcp port 4444 and will inverse all text received on that port.
 - uppercase: open tcp port 4445 and will return the uppercase of all text received on that port.
 - inverse_and_uppercase: open tcp port 4446 and will use the two other containers to inverse and uppercase.

Only the port 4446 is exposed on the host.

Build with:

    docker compose build

Run with:

    docker compose up

Test using netcat:

    echo "test message" | nc -q 1 0.0.0.0 4446

You should see `EGASSEM TSET` on the console.
