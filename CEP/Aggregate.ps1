Get-ChildItem -Directory .\Alg1 | foreach {

    $directory = $_.FullName + "\Regression"
    Get-ChildItem -Path $directory | foreach {

        $content = Import-Csv -Delimiter " " -Path $_.FullName
        $target = "C:\Users\Beni\CEP\" + $_.Name

        Add-Content -Value $content -Path $target
    }
}