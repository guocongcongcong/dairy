#fileinput-bootstrap简单使用

> 因为手上一个小项目使用的是bootstrap做的页面组织，而组里面现有的图片加载上传稍微有点儿丑，而且不能达到甲方的要求，所以就找到了这个插件。因为api是英文的所以开始还是有点小问题的，不过这些都还是能克服的。
> 
>因为项目里是直接把图片数据直接储存到oracle数据据库里面，回显上稍微有点儿不一样。


<!-- TOC depthFrom:2 -->

- [资料](#%E8%B5%84%E6%96%99)
- [功能](#%E5%8A%9F%E8%83%BD)
- [代码](#%E4%BB%A3%E7%A0%81)

<!-- /TOC -->

## 资料

- [github](https://github.com/kartik-v/bootstrap-fileinput)：https://github.com/kartik-v/bootstrap-fileinput
- [csdn-较全的中文api](https://blog.csdn.net/u012526194/article/details/69937741)：https://blog.csdn.net/u012526194/article/details/69937741
- [英文原版-api](http://plugins.krajee.com/file-input#top)：http://plugins.krajee.com/file-input#top
- [英文demo](http://plugins.krajee.com/file-theme-demo#theme-fas)：http://plugins.krajee.com/file-theme-demo#theme-fas

## 功能

- 上传前：加载，删除，上传
- 上传后：回显，删除

## 代码

```html
<!--这个引入是模仿的ajax返回的bolb的数据流-->
<!--
    photos.json:
       var data =  {"photos":"/9j/4AAQSkZJRgABAQAAAQA....",
                    "uuid":"25ab011f338f41bebcc55a94d4aaf03f"}
-->
<script src="../photos.json" type="text/javascript"></script>

<form enctype="multipart/form-data">
  <div class="form-group">
            <div class="file-loading">
                <label>Preview File Icon</label>
                <input id="file-3" type="file" multiple>
            </div>
        </div>
</form>
```

> form表单需要使用：enctype="multipart/form-data"

```js
//这有个坑：
//这里单独说一句：如果是使用的是$(document).ready(...这种方式，那么在html中不要添加class= file
//不然的初始化是完成不了的。
$(document).ready(function () {
    //得到photos的长度
    var len = ''+data.photos+''.length
    var url = baseURL+"users/user/delPhotosCtrl"
    //数据回显的数据需要加载成为img 才能正常回显
    // style需要使用：
    //style=\"width: auto;height: auto;max-width: 100%;max-height: 100%;\" 
    var initialPreview= [
            "<img  style=\"width: auto;height: auto;max-width: 100%;max-height: 100%;\" class=\"file-preview-image \"  src=\"data:image/png;base64,"+data.photos+"\"/>"
            ];
    //caption：图片名称，size：大小，width：宽度，url：删除访问地址，key：删除id

    //initialPreview: [
    //     "http://lorempixel.com/1920/1080/nature/1",
    //     "http://lorempixel.com/1920/1080/nature/2",
    //     "http://lorempixel.com/1920/1080/nature/3"
    //     ],
    //initialPreviewConfig: [
    //     {caption: "nature-1.jpg", size: 329892, width: "120px", url: "{$url}", key: 1},
    //     {caption: "nature-2.jpg", size: 872378, width: "120px", url: "{$url}", key: 2},
    //     {caption: "nature-3.jpg", size: 632762, width: "120px", url: "{$url}", key: 3}
    //      ]
    //如果你使用的是这种加载方式，url就不要改变，直接使用 "{$url}",就可以了。
    //如果使用的是和我一样是回显的数据或者储存到数据里的的话需要单独写一个地址
    var initialPreviewConfig=[{caption: "transport-1.jpg", size: len, width: "120px", url: url, key: data.uuid}]

    $("#file-3").fileinput({
        theme: 'fas',
        //上传地址，比如："http://127.0.0.1/testDemo/fileupload/upload.do", //上传的地址
        'uploadUrl': "http://127.0.0.1/testDemo/fileupload/upload.do", //上传的地址
        //这里是用来添加上传是附带的数据的
        //uploadExtraData:{"id": 1, "fileName":'123.mp3'},
        showUpload: false,
        showCaption: false,
        overwriteInitial: false,
        //这里是个坑：
        //默认使用true，这里需要修改为false
        //资料地址:
        //https://github.com/kartik-v/bootstrap-fileinput/issues/669
        initialPreviewAsData: false,
        initialPreview: initialPreview,
        initialPreviewConfig: initialPreviewConfig
        });
});
```

>先这样，有时间粘一下java代码，看之后的心情
