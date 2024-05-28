cat <<EOT > script.sh
#!/bin/bash
for i in {1..10000}
do
  curl -s -o /dev/null -X POST http://billing:8080/add?client_id=&amount=1000
  curl -s -o /dev/null http://billing:8080/getallt
done
EOT
bash script.sh