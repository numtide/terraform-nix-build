variable "path" {
  type        = string
  description = "Path to build"
}

variable "attributes" {
  type        = list(string)
  description = "A list of Nix attributes to build"
}

variable "args" {
  type        = list(string)
  description = "Extra arguments to pass to nix-build"
  default     = []
}

### Main ###

data "external" "nix_build" {
  program = ["${path.module}/nix-build.py", jsonencode({
    path       = var.path
    args       = var.args
    attributes = var.attributes
  })]
  # Don't use the query argument, it only accepts map(string)
}

### Outputs ###

output "result" {
  description = "Result of the nix-build. A map of attribute to store path."
  value       = data.external.nix_build.result
}
