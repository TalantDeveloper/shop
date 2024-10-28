window.onload = function () {
    document.body.style.zoom = "100%";
};


document.addEventListener('DOMContentLoaded', function () {
    var ua = navigator.userAgent.toLowerCase();
    var is_safari = (ua.indexOf("safari/") > -1 && ua.indexOf("chrome") < 0);

    if (is_safari) {
        var video = document.getElementById('#video-bg');
        video.muted = true;
        video.playsInline = true;

        video.addEventListener('canplaythrough', function () {
            setTimeout(function () {
                video.play().catch(function (error) {
                    console.error('Error attempting to play video:', error);
                });
            }, 50);
        }, false);

        video.load();
    }
});

document.addEventListener('DOMContentLoaded', async () => {
    var swiper = new Swiper(".mySwiper", {
        centeredSlides: true,
        mousewheel: false,
        slidesPerView: 1.2,
        spaceBetween: 12,
        forceToAxis: true,
        observer: true,
        observeParents: true,
        parallax: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            2000: {
                slidesPerView: 4,
                spaceBetween: 35,
            },
            1050: {
                slidesPerView: 3.5,
                spaceBetween: 35,
            },
            768: {
                slidesPerView: 3,
                spaceBetween: 20
            },
            576: {
                slidesPerView: 3,
                spaceBetween: 16
            },
            400: {
                slidesPerView: 2,
                spaceBetween: 12
            },
            320: {
                slidesPerView: 1.6,
                spaceBetween: 12
            }
        },
        on: {
            init: function () {
                this.slideTo(2);
            }
        }
    });
});


function initializeSwiper() {
    const isMobile = window.innerWidth <= 768; // Измените ширину на вашу, если нужно

    return new Swiper(".cardSwiper", {
        direction: isMobile ? "horizontal" : "vertical",
        mousewheel: {
            forceToAxis: true,
            sensitivity: 1,
            thresholdDelta: 50, 
            thresholdTime: 500,
            eventsTarget: '.cardSwiper',
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
    });
}

let swiper2 = initializeSwiper();

window.addEventListener('resize', () => {
    swiper2.destroy(); // Уничтожаем старый экземпляр
    swiper2 = initializeSwiper(); // Создаем новый экземпляр
});


let header_burger = document.querySelector(".header__content-burger");
let burger = document.querySelector(".burger");
let size = document.querySelectorAll(".size");

header_burger.addEventListener("click", () => {
    if (burger.classList[1] != "active") {
        header_burger.classList.add("active");
        burger.classList.add("active");
        document.body.style.overflow = "hidden";
        document.documentElement.style.overflow = "hidden";
    } else {
        header_burger.classList.remove("active");
        burger.classList.remove("active");
        document.body.style.overflow = "unset";
        document.documentElement.style.overflow = "unset";
    }
});

document.addEventListener("DOMContentLoaded", function () {
    let x = 0;

    function handleClick(event) {
        if (event.target.closest(".header__content-burger")) {
            return;
        } else {
            if (burger) {
                if (burger?.classList[1] == "active") {
                    x += 1;
                    if (x == 2) {
                        header_burger.classList.remove("active");
                        burger.classList.remove("active");
                        x = 0;
                        document.body.style.overflow = "unset";
                        document.documentElement.style.overflow = "unset";
                    }
                }
            }

        }
    }

    document.addEventListener("click", handleClick);
    document.addEventListener("touchstart", handleClick);
});

size.forEach((element) => {
    element.addEventListener("click", () => {
        element.classList.toggle("active");
    });
});

let contactBtn = document.querySelectorAll('.cart-modal__content-middle--btn2')
let contactBox = document.querySelector('.contact')
let contactFilter = document.querySelector('.contact-filter')


let cart_btn = document.querySelectorAll(".cart-btn");
let cart_modal = document.querySelector(".cart-modal");
let close_modal_btn = document.querySelector(".close-modal-btn");
let cart_content_middle = document.querySelector(".cart-modal__content-middle");
let cart_content_middle_btn1 = document.querySelector(
    ".cart-modal__content-middle--btn1"
);
let cart_content_bottom = document.querySelector(".cart-modal__content-bottom");
let cart_back = document.querySelector(".back");

contactBtn?.forEach(el => {
    el.addEventListener("click", () => {
        console.log('hello')
        contactBox.classList.add('active')
        cart_modal.classList.remove('active')
        document.body.style.overflow = "hidden";
    })
})

contactFilter?.addEventListener('click', () => {
    contactBox.classList.remove('active')
    document.body.style.overflow = "unset";
    document.documentElement.style.overflow = "unset";
})


cart_btn.forEach((el) => {
    el.addEventListener("click", () => {
        cart_modal.classList.add("active");
        document.body.style.overflow = "hidden";
        document.documentElement.style.overflow = "hidden";
    });
});

close_modal_btn.addEventListener("click", () => {
    cart_modal.classList.remove("active");
    cart_content_middle.classList.remove("off");
    cart_content_bottom.classList.remove("active");
    document.body.style.overflow = "unset";
    document.documentElement.style.overflow = "unset";
});

cart_content_middle_btn1.addEventListener("click", () => {
    cart_content_middle.classList.add("off");
    cart_content_bottom.classList.add("active");
});

cart_back.addEventListener("click", () => {
    cart_content_middle.classList.remove("off");
    cart_content_bottom.classList.remove("active");
});


document.addEventListener("DOMContentLoaded", function() {
    // Находим элемент с уведомлением
    var messageBox = document.querySelector(".messageBox");

    // Проверяем, существует ли элемент
    if (messageBox) {
        // Добавляем класс 'show' для плавного появления
        setTimeout(function() {
            messageBox.classList.add('show');
        }, 100); // небольшая задержка для плавного эффекта

        // Удаляем уведомление через 3 секунды
        setTimeout(function() {
            messageBox.classList.remove('show');
        }, 3000); // Плавное удаление через 3 секунды
    }
});

