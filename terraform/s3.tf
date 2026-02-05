resource "aws_s3_bucket" "iac-example-lsc" {
  bucket = "iac-example-lsc"
  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}