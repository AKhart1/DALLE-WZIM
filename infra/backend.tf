terraform {
  backend "s3" {
    bucket = "dallewzim"
    key    = "webapp/state"
    region = "eu-north-1"
  }
}
