MNISTの保存
----------------------------------

清水研で使うデータ形式になれることを目的とする．

一般的に自然画像で使われるpng, jpg形式では， `unsigned char` (8bits)までしか保存することができない．ただし，ここではtiff形式は考えない．

医用画像は， `short` (16bits) 以上で画像を表現することが多いため，pngなどの形式は用いず，以下のような形式を用いることが多い（私見含む）．

これらの形式は， `double` も保存することができるため，情報をあまり落とすことなく保存することができる．

```
mhd + raw
nii.gz
nrrd
nhdr
dcm
etc...
```

可視化する際は， `3D Slicer` や `PLUTO` などのビューワーを用いることが多い．

使い方については，先輩に聞けば教えてくれる．

当研究室では， `mhd + raw` 形式を用いて，画像を保存することが多いため，本プログラムでは `mnist` を `mhd` と `png` で保存する方法を示す．

### Requirements

```
SimpleITK
chainer
numpy
```

### 使い方

```
usage: save_mnist.py [-h] [--base BASE] [--outputDir OUTPUTDIR]
                     [--save_type SAVE_TYPE]

optional arguments:
  -h, --help            show this help message and exit
  --base BASE, -B BASE  base directory path of program files
  --outputDir OUTPUTDIR, -o OUTPUTDIR
                        Directory to output the result(base path)
  --save_type SAVE_TYPE
                        Save type (mhd or png)
```

#### pngで保存するときの使い方

[0,255]に正規化してから， `unsigned char` で保存する．

```
python save_mnist --save_type png
```

#### mhdで保存するときの使い方

chainerのデフォルトでは，[0,1] に正規化されているため， `float` で保存する．

今回は，解像度は1mmにしてある．

```
python save_mnist --save_type mhd
```
