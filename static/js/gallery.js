$(document).ready(function () {
    let picture = $('.js-fullsize-img')

    $('.js-preview').click(function (e) {
        picture.attr('src', $(e.currentTarget).attr('data-fullsize-url'))
    })
})
