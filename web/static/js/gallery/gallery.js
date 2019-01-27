$(document).ready(function () {
    $(".justified-gallery").justifiedGallery({
    rowHeight : 250,
    lastRow : 'nojustify',
    margins : 15,
    border : 50
}).on('jg.complete', function () {
        $(this).find('a').magnificPopup({
            type: 'image',
            gallery: {
                enabled: true
            },
        })
    })
})
