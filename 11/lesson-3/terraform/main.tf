variable "do_token" {}

variable "name" {
  default = "do-k8s"
}

resource "digitalocean_kubernetes_cluster" "k8s" {
  name   = var.name
  region = "fra1"
  version = "1.22.7-do.0"

  node_pool {
    name = "${var.name}-worker-pool"

    # doctl kubernetes options sizes
    size       = "s-2vcpu-4gb"
    node_count = 2
  }
}

provider "kubernetes" {
  host  = resource.digitalocean_kubernetes_cluster.k8s.endpoint
  token = resource.digitalocean_kubernetes_cluster.k8s.kube_config[0].token
  cluster_ca_certificate = base64decode(
    resource.digitalocean_kubernetes_cluster.k8s.kube_config[0].cluster_ca_certificate
  )
}