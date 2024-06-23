resource "aws_eip" "webapp_eip" {
  vpc = true
}

resource "aws_instance" "webapp_host" {
  ami           = "ami-0705384c0b33c194c"
  instance_type = "t3.micro"
  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name

  user_data = file("${path.module}/scripts/ec2.sh") 

  tags = {
    Name = "WebApp"
  }

  key_name        = "WebAppKey"
  vpc_security_group_ids = [aws_security_group.webapp.id]
}

resource "aws_eip_association" "eip_assoc" {
  instance_id = aws_instance.webapp_host.id
  allocation_id = aws_eip.webapp_eip.id
}
