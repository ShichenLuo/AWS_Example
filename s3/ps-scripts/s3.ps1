Import-Module AWS.Tools.S3

$region="us-east-1"

$BucketName=Read-Host -Prompt 'Enter the S3 Bucket Name:'


function BucketExists{
    $bucket=Get-S3Bucket -BucketName $BucketName -ErrorAction SilentlyContinue -ProfileName myprofile
    return $null -ne $bucket
}

if (-not (BucketExists)){
    Write-Host "Create bucket $BucketName, region $region"
    New-S3Bucket -BucketName $BucketName -region $region -ProfileName myprofile
}
else{
    Write-Host "Bucket already exist..."
}


$file_name="hello.txt"
$content="hello world!"
Set-Content -Path $file_name -Value $content
Write-S3Object -BucketName $BucketName -File $file_name -Key $file_name -ProfileName myprofile