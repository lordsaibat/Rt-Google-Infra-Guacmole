resource "null_resource" "guacmole-add-linuxhost"{
   provisioner "local-exec" {
       command = "python3 -W ignore ./support_files/guac-auth.py --user='${var.guac-username}' --pass='${var.guac-password}' --host='${var.guac-host}' --port='${var.guac-port}' | xargs -t -I authToken python3 -W ignore ./support_files/guac-new-host.py --host='${var.guac-host}' --port='${var.guac-port}' --auth=authToken --newhosttype='${var.new-connection-type}' --newhostport='${var.new-connection-port}' --newhostip='${var.new-connection-ip}' --newhostname='${var.new-connection-name}' --newhostusername='${var.new-connection-username}' --newhostprivatekey='${var.new-connection-private-key}'"
   }

   provisioner "local-exec" {
       when = "destroy"
       command = "python3 -W ignore ./support_files/guac-auth.py --user='${var.guac-username}' --pass='${var.guac-password}' --host='${var.guac-host}' --port='${var.guac-port}' | xargs -t -I authToken python3 -W ignore ./support_files/guac-remove-host.py --host='${var.guac-host}' --port='${var.guac-port}' --auth=authToken --hosttodelete=${var.new-connection-name}"
   }
}
