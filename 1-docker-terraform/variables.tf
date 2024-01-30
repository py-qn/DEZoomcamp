variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-creds.json"
}


locals {
  data_lake_bucket = "dtc_data_lake"
}

variable "project" {
  description = "GCP Project ID"
  default     = "dtc-de-412312"
}

variable "region" {
  description = "Region for GCP resources."
  default     = "europe-west6"
  type        = string
}

variable "storage_class" {
  description = "Storage class type"
  default     = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset"
  type        = string
  default     = "trips_data_all"
}

