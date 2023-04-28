/* 
  아래에 코드를 작성해주세요.
*/
const load = document.querySelector('.search-result--loadingList')

const apikey = '9ffb0d35e1c8955d8ad697f6e06d822a'
const search = document.querySelector('.search-box__input')
const btn = document.querySelector('.search-box__button')
const album_lst = document.querySelector('.search-result')

// ==============================================================================================
/* 
===== 
(advanced) Infinite Scrolling
=====
*/
const sentinel = document.createElement('div')
// sentinel.id = 'sentinel'
createObserver(sentinel)

function createObserver(target) {
  console.log(target);
  const getMoreAlbums = (entries) => {
    // entries.forEach(entrie => {
      //   if (entrie.isIntersecting) {
        //     console.log('next page');
        //     console.log(entrie);
        //     console.log(entries);
        //     fetchAlbums()
        //   }
        // })
        if (entries[0].isIntersecting) {
          fetchAlbums()
          // observer.unobserve(target)
          // observer.observe(btn)
        }
      }
      
      const observer = new IntersectionObserver(getMoreAlbums);
      observer.observe(target); 
    }
    
// ===============================================================================================
    

btn.addEventListener('click', fetchAlbums)


function fetchAlbums(event) {
  load.style.display = 'block'
  // album_lst.innerHTML = ''

  // console.log(event.target);
  // console.log(search.value);
  const searchVal = search.value
  // search.value = ''
  axios({
    method:'get',
    url:`https://ws.audioscrobbler.com/2.0/?method=album.search&album=${searchVal}&api_key=${apikey}&format=json`,
  })
  .then((response)=>{
    // console.log(response.data.results);
    const albums = response.data.results.albummatches.album
    return albums
  })
  .then((response)=>{
    // console.log(typeof(response))
    for (const album of response) {
      // console.log(album);
      // create card element
      const result_album = document.createElement('div')
      const album_img = document.createElement('img')
      const result_txt = document.createElement('div')
      const inner1 = document.createElement('h2')
      const inner2 = document.createElement('p')

      // attribute
      album_img.setAttribute('src', album.image[1]['#text'])
      result_album.classList.add('search-result__card')
      result_txt.classList.add('search-result__text')
      inner1.innerHTML = album.name
      inner2.innerHTML = album.artist

      // append
      result_txt.appendChild(inner1)
      result_txt.appendChild(inner2)
      result_album.appendChild(album_img)
      result_album.appendChild(result_txt)
      album_lst.appendChild(result_album)

      result_album.appendChild(sentinel)


      load.style.display = 'none'
    }
  })
}
