// const bar = document.getElementById('bar');
// const nav = document.getElementById('navbar');
// if (bar) {
//     bar.addEventListener('click' , () => {
//         nav.classList.add('active');
//     })
// }


// sproduct script

var MainImg = document.getElementById("MainImg");
        var smallimg=document.getElementsByClassName("small-img");

        smallimg[0].onclick=function(){
            MainImg.src=smallimg[0].src;
        }

        smallimg[1].onclick=function(){
            MainImg.src=smallimg[1].src;
        }

        smallimg[2].onclick=function(){
            MainImg.src =smallimg[2].src;
        }

        smallimg[3].onclick=function(){
            MainImg.src=smallimg[3].src;
        }
        

        function myfunction(){
            window.open("shop.html");
        }
        
        function function1(){
            window.open("chart.html");
        }