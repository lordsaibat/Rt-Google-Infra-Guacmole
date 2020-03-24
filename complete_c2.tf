terraform {
  required_version = ">= 0.11.0"
}

module "http-c2" {
    source = "./modules/google/http-c2"
    project = "redteam-"
}

module "guac-connection-http-c2" {
  source = "./modules/guacmole"
  guac-host = "192.168.2.28"
  guac-port = "8443" 
  guac-username = "guacadmin"
  guac-password = "guacadmin"

  new-connection-name = "http-c2"
  new-connection-type = "ssh"
  new-connection-port = "22"
  new-connection-ip = "${module.http-c2.ip}"
  new-connection-username = "guser"
  new-connection-public-key = "${file("./ssh_keys/gkeys.pub")}"
  new-connection-private-key = "${file("./ssh_keys/gkeys")}"
}

output "http-c2-ip" {
  value = "${module.http-c2.ip}"
}


