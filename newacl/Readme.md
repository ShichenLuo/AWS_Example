# change bucket ownership

aws s3api put-bucket-ownership-controls \
--bucket my-example-lsc \
--ownership-controls "Rules=[{ObjectOwnership=BucketOwnerEnforced}]" \
--profile myprofile


aws s3api put-bucket-policy \
--bucket my-example-lsc \
--policy file://newacl/policy.json \
--profile myprofile

