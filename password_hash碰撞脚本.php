<?php
// 假设这是你要匹配的目标密文（哈希值）
$targetHash = '$2a$10$7JB720yubVSZvUI0rEqK/.VqGOZTH.ulu33dHOiBE8ByOhJIrdAu2'; // 示例密文

// 使用正斜杠修改文件路径
$passwordsFile = "D:/Tools/2-字典/常用密码.txt";  // 确保路径正确

// 检查文件是否存在
if (!file_exists($passwordsFile)) {
    die("文件不存在: $passwordsFile\n");
}

$handle = fopen($passwordsFile, "r");

if ($handle) {
    // 遍历每一行密码
    while (($line = fgets($handle)) !== false) {
        // 去除每行的换行符和空格
        $password = trim($line);

        echo($targetHash . "-----". $password);
        echo "\n";

        // 检查哈希是否匹配
        if (password_verify($password, $targetHash)) {
            echo "找到了匹配的密码: " . $password . "\n";
            break;  // 找到后退出循环
        }
    }
    
    fclose($handle);
} else {
    echo "无法打开文件。\n";
}
?>
