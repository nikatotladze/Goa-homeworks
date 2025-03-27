// 2

// Bubbling და Capturing არის ორი გზა, რომლის საშუალებითაც ღონისძიება ვრცელდება DOM-ის სტრუქტურაში.
// როდესაც მომხმარებელი რაიმე ელემენტზე კლიკს აკეთებს, ეს ღონისძიება არ რჩება მხოლოდ ამ ელემენტზე – ის შეიძლება გავრცელდეს მშობელ ელემენტებამდე. 

// 3

const images = [
    "https://www.google.com/imgres?q=picture%20of%20georgia&imgurl=https%3A%2F%2Fwww.state.gov%2Fwp-content%2Fuploads%2F2023%2F07%2Fshutterstock_129551402v2.jpg&imgrefurl=https%3A%2F%2Fwww.state.gov%2Fcountries-areas%2Fgeorgia%2F&docid=RQ18C3HXGW1QvM&tbnid=HQSCQAryUsvGfM&vet=12ahUKEwjdp-X23piMAxUz2AIHHSFjGFAQM3oECHgQAA..i&w=2560&h=1839&hcb=2&ved=2ahUKEwjdp-X23piMAxUz2AIHHSFjGFAQM3oECHgQAA",
    "https://www.google.com/imgres?q=picture%20of%20georgia&imgurl=https%3A%2F%2Fstorage.georgia.travel%2Fimages%2Ftbilisi-picture.webp&imgrefurl=https%3A%2F%2Fgeorgia.travel%2F&docid=RW2j2vYPPJktIM&tbnid=xUd0PuHsUJoBDM&vet=12ahUKEwjdp-X23piMAxUz2AIHHSFjGFAQM3oECBcQAA..i&w=1920&h=1080&hcb=2&ved=2ahUKEwjdp-X23piMAxUz2AIHHSFjGFAQM3oECBcQAA",
    "https://www.google.com/imgres?q=picture%20of%20georgia&imgurl=https%3A%2F%2Ftourguide.ge%2Fwp-content%2Fuploads%2F2020%2F02%2Fgoeirge-national-parks.jpeg%3Fv%3D1621426231&imgrefurl=https%3A%2F%2Ftourguide.ge%2Fintroducing-georgia%2F&docid=DCzRz52UvAT9cM&tbnid=Cyb8PGxjAEeaPM&vet=12ahUKEwjdp-X23piMAxUz2AIHHSFjGFAQM3oECDsQAA..i&w=1900&h=1266&hcb=2&ved=2ahUKEwjdp-X23piMAxUz2AIHHSFjGFAQM3oECDsQAA"
];
        let index = 0;

        function updateImage() {
            document.getElementById("slider").src = images[index];
        }

        function prev() {
            index = (index - 1 + images.length) % images.length;
            updateImage();
        }

        function next() {
            index = (index + 1) % images.length;
            updateImage();
        }



// 4

        const Images = [
            "https://www.google.com/imgres?q=programing&imgurl=https%3A%2F%2Fwww.lightsregionalinnovation.com%2Fwp-content%2Fuploads%2F2021%2F03%2F704318ee9be94acabf28919a734951b8-scaled.jpg&imgrefurl=https%3A%2F%2Fwww.lightsregionalinnovation.com%2F2017%2F08%2F18%2Fwhere-to-start-with-programing%2F&docid=FBlfcANhHPJV-M&tbnid=83RnSjVa_xlffM&vet=12ahUKEwiDxJHE45iMAxW-3gIHHQ-fFmUQM3oECBgQAA..i&w=2560&h=1709&hcb=2&ved=2ahUKEwiDxJHE45iMAxW-3gIHHQ-fFmUQM3oECBgQAA",
            "https://www.google.com/imgres?q=programing&imgurl=https%3A%2F%2Fi0.wp.com%2Fgaronpower.com%2Fwp-content%2Fuploads%2F2019%2F01%2Fcomputer-programming.jpeg%3Ffit%3D1500%252C1000%26ssl%3D1&imgrefurl=https%3A%2F%2Fgaronpower.com%2Flaunched-into-the-world-of-computer-programing%2F&docid=FHdIZW4EPoQNkM&tbnid=q2V58e-O_P7A5M&vet=12ahUKEwiDxJHE45iMAxW-3gIHHQ-fFmUQM3oFCIQBEAA..i&w=1500&h=1000&hcb=2&ved=2ahUKEwiDxJHE45iMAxW-3gIHHQ-fFmUQM3oFCIQBEAA",
            "https://www.google.com/imgres?q=programing&imgurl=https%3A%2F%2Fcdn-0.securityonline.info%2Fwp-content%2Fuploads%2F2020%2F02%2Fstring-code.png&imgrefurl=https%3A%2F%2Fsecurityonline.info%2Fcoding-for-kids-why-young-students-should-learn-programing%2F&docid=ccxeSPHktjBpUM&tbnid=j_tpAS-ky8YDmM&vet=12ahUKEwiDxJHE45iMAxW-3gIHHQ-fFmUQM3oECBkQAA..i&w=1147&h=768&hcb=2&ved=2ahUKEwiDxJHE45iMAxW-3gIHHQ-fFmUQM3oECBkQAA",
            "https://www.google.com/imgres?q=programing&imgurl=https%3A%2F%2Fwww.catalyst-ca.net%2Fwp-content%2Fuploads%2F2021%2F12%2Ftop-programing-languages.jpeg&imgrefurl=https%3A%2F%2Fwww.catalyst-ca.net%2Ffr%2Fblog%2Ftop-programming-languages-selection-criteria&docid=6mNtwRkxf4rgGM&tbnid=KQvLJqqOcFA58M&vet=12ahUKEwiDxJHE45iMAxW-3gIHHQ-fFmUQM3oECGMQAA..i&w=900&h=600&hcb=2&ved=2ahUKEwiDxJHE45iMAxW-3gIHHQ-fFmUQM3oECGMQAA"
        ];
        
        let Index = 0;

        function updateImage() {
            document.getElementById("slider").src = images[index];
        }

        function prev() {
            index = (index - 1 + images.length) % images.length;
            updateImage();
        }

        function next() {
            index = (index + 1) % images.length;
            updateImage();
        }


    

// 5

document.getElementById("userForm").addEventListener("submit", function(event) {
    event.preventDefault(); // გვერდის გადატვირთვის თავიდან ასაცილებლად

    // Input ველებიდან მონაცემების აღება
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let age = document.getElementById("age").value;

    // შედეგის გამოტანა გვერდზე
    document.getElementById("result").innerHTML = 
        `<p><strong>Name:</strong> ${name}</p>
         <p><strong>Email:</strong> ${email}</p>
         <p><strong>Age:</strong> ${age}</p>`;
});