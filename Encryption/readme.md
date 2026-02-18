




## create key
aws kms create-key --description "my example key" --profile myprofile --region us-east-1

## create alias for the key
aws kms create-alias \
--alias-name alias/my-research-key \
--target-key-id 790ff123-36b6-447f-8183-9e6ce43a3cc8 \
--region us-east-1 \
--profile myprofile \
--region us-east-1

## delete key
aws kms schedule-key-deletion \
  --key-id 790ff123-36b6-447f-8183-9e6ce43a3cc8 \
  --pending-window-in-days 7 \
  --profile myprofile

## delete alias
aws kms delete-alias \
  --alias-name alias/my-research-key \
  --profile myprofile \
  --region us-east-1


## Put object with SSEKMS
aws s3api put-object \
--bucket my-example-lsc \
--key test-files/hello.txt \
--body test-files/hello.txt \
--server-side-encryption aws:kms \
--ssekms-key-id 790ff123-36b6-447f-8183-9e6ce43a3cc8 \
--profile myprofile


## Put object with SSE-C
### create key
%%% openssl rand -base64 32
### upload
aws s3api put-object \
  --bucket my-example-lsc \
  --key test-files/hello.txt \
  --body test-files/hello.txt \
  --sse-customer-algorithm AES256 \
  --sse-customer-key q83nXhRk3kKx9Jw8kP4mZ1bYw6sL2tQvU9rT5yZc0xA=
### download
aws s3api get-object \
  --bucket my-example-lsc \
  --key test-files/hello.txt \
  output.txt \
  --sse-customer-algorithm AES256 \
  --sse-customer-key q83nXhRk3kKx9Jw8kP4mZ1bYw6sL2tQvU9rT5yZc0xA=