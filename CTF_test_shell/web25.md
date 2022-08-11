> mt_rand()函数每次执行的值是不一样的，呈线性关系

~~~php
<?php 
mt_srand(372619038); 
echo mt_rand()."\n";
echo mt_rand()."\n";
echo mt_rand()."\n";
?>

//结果分别为 1155388967 125197722 1461103528 
~~~

> 通过php_mt_seed脚本来生成种子 
>下载链接：https://www.openwall.com/php_mt_seed/
> 
>爆破出随机种子
>
>然后把随机种子放入上面的代码即可获得第二次和第三次mt_rand()随机值的和

~~~php
<?php 
mt_srand(1338537082); 
echo mt_rand()."\n";
echo intval(mt_rand())+intval(mt_rand())."\n";
?>
~~~

