// 1

fetch('https://fakestoreapi.com/products/1')
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.log('შეცდომა:', error);
  });



// 2

fetch('https://fakestoreapi.com/products')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP შეცდომა! სტატუსი: ${response.status}`);
    }
    return response.json();
  })
  .then(products => {
    console.log('მიღებული პროდუქტები:', products);
  })
  .catch(error => {
    console.error('შეცდომა მონაცემების მიღებისას:', error);
  });


// 3

document.getElementById('book-form').addEventListener('submit', async function (e) {
  e.preventDefault();
  
  const query = document.getElementById('search-input').value;
  const resultsDiv = document.getElementById('results');
  resultsDiv.innerHTML = 'მონაცემების ჩატვირთვა...';

  try {
    const response = await fetch(`https://www.googleapis.com/books/v1/volumes?q=${encodeURIComponent(query)}`);
    const data = await response.json();
    
    resultsDiv.innerHTML = '';

    if (!data.items || data.items.length === 0) {
      resultsDiv.innerHTML = '<p>ვერ მოიძებნა წიგნი.</p>';
      return;
    }

    data.items.forEach(item => {
      const book = item.volumeInfo;
      const title = book.title || 'სათაური მიუწვდომელია';
      const publishedDate = book.publishedDate || 'გამოშვების თარიღი მიუწვდომელია';
      const description = book.description ? book.description.slice(0, 300) + '...' : 'აღწერა მიუწვდომელია';
      const pageCount = book.pageCount || 'უცნობია';
      const image = book.imageLinks?.thumbnail || '';

      const bookDiv = document.createElement('div');
      bookDiv.className = 'book';

      bookDiv.innerHTML = `
        <img src="${image}" alt="წიგნის სურათი">
        <div class="book-info">
          <h2>${title}</h2>
          <p><strong>გამოშვების წელი:</strong> ${publishedDate}</p>
          <p><strong>გვერდების რაოდენობა:</strong> ${pageCount}</p>
          <p><strong>აღწერა:</strong> ${description}</p>
        </div>
      `;

      resultsDiv.appendChild(bookDiv);
    });

  } catch (error) {
    resultsDiv.innerHTML = '<p>შეცდომა მოხდა მონაცემების მიღებისას.</p>';
    console.error(error);
  }
});
