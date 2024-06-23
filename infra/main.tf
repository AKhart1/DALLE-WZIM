resource "aws_instance" "webapp_host" {
  ami           = "ami-0705384c0b33c194c"
  instance_type = "t3.micro"

  user_data = file("${path.module}/scripts/ec2.sh") 

  tags = {
    Name = "WebApp"
  }

  key_name        = "WebAppKey"
  vpc_security_group_ids = [aws_security_group.webapp.id]
}
