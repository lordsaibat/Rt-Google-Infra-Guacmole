provider "google" {
  project = var.project
  credentials = file("gcloud.json")
}

resource "google_compute_instance" "http-c2" {
  name         = "http-c2"
  machine_type = "n1-standard-1"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  // Local SSD disk
  scratch_disk {
    interface = "SCSI"
  }

  network_interface {
    network = google_compute_network.default.name

    access_config {
      // Ephemeral IP
    }
  }

  metadata = {
   ssh-keys = "guser:${file("./ssh_keys/gkeys.pub")}"
 }

 //Upload all the directories on local host files
  provisioner "file" {
	  source      = "./files/"
    destination = "/tmp/"
		
        connection {
        type = "ssh"
        host = self.network_interface.0.access_config.0.nat_ip
        user = "guser"
        private_key = "${file("./ssh_keys/gkeys")}"
        }
  }


   provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y docker-compose curl",
      "curl -fsSL get.docker.com -o get-docker.sh",
      "sudo sh get-docker.sh",
      "sudo docker-compose -f /tmp/metasploit-docker/docker-compose.yml up -d",
    ]

    connection {
      host = self.network_interface.0.access_config.0.nat_ip
      type = "ssh"
      user = "guser"
      private_key = "${file("./ssh_keys/gkeys")}"
    }
  }
}

resource "google_compute_firewall" "http-c2-firewall-hhtp" {
  name    = "http-c2-firewall-http"
  network = google_compute_network.default.name

  allow {
    protocol = "tcp"
    ports    = ["80", "443" ]
  }
   source_ranges = ["0.0.0.0/0"]
   direction = "INGRESS"

  source_tags = ["http-c2"]
}

resource "google_compute_firewall" "http-c2-firewall-ssh" {
  name    = "http-c2-firewall-ssh"
  network = google_compute_network.default.name

  allow {
    protocol = "tcp"
    ports    = ["22" ]
  }
   source_ranges = ["0.0.0.0/0"] 
   direction = "INGRESS"

  source_tags = ["http-c2"]
}


resource "google_compute_network" "default" {
  name = "http-c2-network"
}