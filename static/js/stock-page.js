// stock
(function () {
    const csrftoken = getCookie('csrftoken')

    toggleStockPinned()
    function toggleStockPinned(){
        const matches = document.querySelectorAll('.cs-event-toggle-pinned')
        matches.forEach(it => {
            it.addEventListener('click', function (e) {
                e.preventDefault()
                // console.log(e.target)
                // console.log(it.innerHTML)
                doEventPinned(it)
            })
        })
    }
    function doEventPinned(self){
        // console.log(self)
        // console.log(self.dataset.pinned)
        const is_pinned = (self.dataset.pinned === 'true')
        const stock_symbol = self.dataset.stock
        // console.log(self.dataset)

        if(is_pinned){
            // 이미 관심종목에 등록된 것을 토글하면, 등록해제를 진행.
            url = `/stock/toggle_stock_pinned/deactivate/${stock_symbol}/`
        } else {
            // 관심종목에 등록
            url = `/stock/toggle_stock_pinned/activate/${stock_symbol}/`
        }
        
        // console.log(url)
        // document.getElementById("ajaxButton").addEventListener('click', makeRequest);
        // makeRequest(link)
        
        
        doAjaxFetch(url, (text) => {
            self.innerHTML = renderStockPinned((is_pinned === false))
            self.dataset.pinned = (is_pinned === false)
        })
    }

    function doAjaxFetch(url, onSuccess){
        const headers = new Headers();
        headers.append('X-CSRFToken', getCookie('csrftoken'));
    
        fetch(url, {
            method: 'POST',
            headers,
            mode: 'same-origin'  // Do not send CSRF token to another domain.
        }).then(function(response) {
            response.text().then(function(text){
                // console.log(text)
                onSuccess(text)
            })
        });
    }

    function renderStockPinned(is_pinned){
        if(is_pinned){
            // console.log('True')
            return `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bookmarks-fill" viewBox="0 0 16 16">
                        <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4z"/>
                        <path d="M4.268 1A2 2 0 0 1 6 0h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L13 13.768V2a1 1 0 0 0-1-1H4.268z"/>
                    </svg>`
        } else {
            // console.log('False')
            return `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bookmarks" viewBox="0 0 16 16">
                        <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                        <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
                    </svg>`
        }
    }
    
    /**
     * CSRF 를 위한 부분
     * @param {str} name 
     * @returns 
     */
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
})();