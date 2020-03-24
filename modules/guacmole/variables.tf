variable "guac-host" {
    default = "127.0.0.1"
}

variable "guac-port" {
    default = "8433"
}

variable "guac-username" {
    default = "user"
}

variable "guac-password" {
    default = "password"
}

variable "guac-auth-token" {
    default = ""
}
variable "new-connection-name" {
    default = "new-connection-name"
}

variable "new-connection-type" {
    default = "ssh" //ssh,telnet,vnc,rdp
}

variable "new-connection-port" {
    default = "22"
}

variable "new-connection-ip" {
    default = "127.0.0.1"
}

variable "new-connection-username" {
    default = ""
}

variable "new-connection-password" {
    default = ""
}

variable "new-connection-public-key" {
    default = ""
}

variable "new-connection-private-key" {
    default = ""
}

variable "new-connection-security" {
    default = "any" //RDP Security: any, nla, rdp, tls
}

variable "new-connection-ignore-cert" {
    default = "false" 
}