/*
====================================================
 AgriNova AI v2.0
 Global Application JavaScript
====================================================
*/


"use strict";



/* ==============================
   Application Configuration
============================== */


const AgriNova = {


    apiBase: "",


    loader: null,


    init() {


        this.loader =
            document.getElementById("loader");


        this.setupSidebar();


        this.setupGlobalForms();


        this.hideLoader();


        console.log(
            "AgriNova AI v2.0 initialized"
        );


    }



};





/* ==============================
   Loader Management
============================== */


AgriNova.showLoader = function(){


    if(this.loader){

        this.loader.style.display =
            "flex";

    }

};



AgriNova.hideLoader = function(){


    if(this.loader){

        this.loader.style.display =
            "none";

    }

};





/* ==============================
   Sidebar Toggle
============================== */


AgriNova.setupSidebar = function(){


    const toggle =
        document.getElementById(
            "sidebarToggle"
        );


    const sidebar =
        document.querySelector(
            ".sidebar-wrapper"
        );


    if(toggle && sidebar){


        toggle.addEventListener(
            "click",
            function(){


                sidebar.classList.toggle(
                    "show"
                );


            }
        );


    }


};





/* ==============================
   Toast Notification
============================== */


AgriNova.toast = function(
    message,
    type="success"
){


    const toastElement =
        document.getElementById(
            "liveToast"
        );


    const toastBody =
        document.getElementById(
            "toastMessage"
        );


    if(
        toastElement &&
        toastBody
    ){


        toastBody.innerHTML =
            message;



        toastElement.className =
            "toast align-items-center text-bg-"
            + type;



        const toast =
            new bootstrap.Toast(
                toastElement
            );


        toast.show();


    }

};





/* ==============================
   API Helper
============================== */


AgriNova.request = async function(
    url,
    options={}
){


    try{


        this.showLoader();



        const response =
            await fetch(
                this.apiBase + url,
                {

                    headers: {

                        "Content-Type":
                        "application/json"

                    },


                    ...options

                }
            );



        const data =
            await response.json();



        if(!response.ok){


            throw new Error(
                data.message ||
                "API Error"
            );


        }


        return data;



    }


    catch(error){


        console.error(
            error
        );


        this.toast(
            error.message,
            "danger"
        );


        return null;


    }


    finally{


        this.hideLoader();


    }


};





/* ==============================
   Form Protection
============================== */


AgriNova.setupGlobalForms =
function(){


    document
    .querySelectorAll(
        "form"
    )
    .forEach(
        form=>{


            form.addEventListener(
                "submit",
                function(){

                    AgriNova.showLoader();

                }
            );


        }
    );


};





/* ==============================
   Date Formatter
============================== */


AgriNova.formatDate =
function(date){


    return new Date(date)
    .toLocaleDateString();


};





/* ==============================
   Number Formatter
============================== */


AgriNova.formatNumber =
function(value){


    return Number(value)
    .toLocaleString();


};





/* ==============================
   DOM Ready
============================== */


document.addEventListener(
    "DOMContentLoaded",
    function(){


        AgriNova.init();


    }
);