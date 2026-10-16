variable "aws_region" {
  description = "AWS region for the temporary course demonstration."
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  type    = string
  default = "orbit-capstone"
  validation {
    condition     = can(regex("^[a-z][a-z0-9-]{2,28}$", var.project_name))
    error_message = "Use 3–29 lowercase letters, digits, and hyphens, starting with a letter."
  }
}

variable "kubernetes_version" {
  description = "Verify regional availability with aws eks describe-cluster-versions before apply."
  type        = string
  default     = "1.36"
}

variable "admin_cidrs" {
  description = "Public IPv4 CIDRs allowed to reach the EKS API (include your workstation /32)."
  type        = list(string)
  validation {
    condition = length(var.admin_cidrs) > 0 && alltrue([
      for cidr in var.admin_cidrs : can(cidrnetmask(cidr)) && cidr != "0.0.0.0/0"
    ])
    error_message = "Provide restricted IPv4 CIDRs; the public API cannot be open to the world."
  }
}

variable "node_instance_type" {
  type    = string
  default = "t3.medium"
}

variable "node_count" {
  type    = number
  default = 2
  validation {
    condition     = var.node_count >= 1 && var.node_count <= 3 && floor(var.node_count) == var.node_count
    error_message = "Choose one to three worker nodes for this capstone."
  }
}

variable "deploy_principal_arn" {
  description = "Optional existing IAM role ARN for CI; its trust policy must restrict GitHub OIDC to this repository and environment."
  type        = string
  default     = ""
}
