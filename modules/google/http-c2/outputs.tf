output "ip" {
 value = "${google_compute_instance.http-c2.network_interface.0.access_config.0.nat_ip}"
}


output "ssh_user" {
  value = "root"
}