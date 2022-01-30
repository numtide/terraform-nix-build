# terraform-nix-build

Build Nix with the external provider

## Requirements

`nix-build` and `python3` installed on the host.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_external"></a> [external](#provider\_external) | 2.2.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [external_external.nix_build](https://registry.terraform.io/providers/hashicorp/external/latest/docs/data-sources/external) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_args"></a> [args](#input\_args) | Extra arguments to pass to nix-build | `list(string)` | <pre>[<br>  "--no-out-link"<br>]</pre> | no |
| <a name="input_attributes"></a> [attributes](#input\_attributes) | A list of Nix attributes to build | `list(string)` | n/a | yes |
| <a name="input_path"></a> [path](#input\_path) | Path to build | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_result"></a> [result](#output\_result) | Result of the nix-build. A map of attribute to store path. |
