local name = "example";
{
  app: {
    name: name,
    version: "1.0",
    replicas: 3,
    containers: [
      {
        name: name,
        image: "example/image:latest",
        ports: [80, 443],
      }
    ]
  }
}
