<#
.DESCRIPTION
增加某个路径下的图片拍摄时间信息，文件名必须是 yyyyMMddHHmmss 这样的形式
.PARAMETER Folder
要查找的路径，默认是当前路径
.PARAMETER Suffix
要查找的文件后缀名，默认是 jpg
.PARAMETER Recurse
是否递归查找，默认不递归
#>

# Parameter
[CmdletBinding()]
param (
    [Parameter(Position = 0)]
    [string]$Folder = ".",
    [Parameter(Position = 1)]
    [string]$Suffix = "jpg",
    [Parameter()]
    [switch]$Recurse
)


<#
.DESCRIPTION
传入 yyyyMMddHHmmss 形式的文件名返回 yyyy:MM:dd HH:mm:ss 这样的字符串
#>
function formatDatetime {

    param (
        [Parameter(Mandatory)]
        [string]$fileName
    )
    return $($fileName.substring(0, 4) + ":" + $fileName.substring(4, 2) + ":" + $fileName.substring(6, 2) + " " + $fileName.substring(8, 2) + ":" + $fileName.substring(10, 2) + ":" + $fileName.substring(12, 2))
    
}

if ($Recurse) {
    $files = Get-ChildItem -LiteralPath $Folder -Recurse -Filter "*.${Suffix}"
}
else {
    $files = Get-ChildItem -LiteralPath $Folder -Filter "*.${Suffix}"
}
foreach ( $f in $files) {
    $v = $(python .\modify-exif.py -f $f.FullName -rt -s)
    if ($v.count -eq 0) {
        $dateTime = $(formatDatetime $f.Name)
        python .\modify-exif.py -f $f.FullName -wt -v $dateTime
    }
}


