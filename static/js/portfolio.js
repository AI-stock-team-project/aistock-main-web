let is_custom_asset = false
// document.getElementById('#handle_pane_before').addEventListener('click', handle_pane_before)
// console.log(document.getElementById("pills-risk-tab"))


class AssetSubPaneHandle {
    SUBPANE_MODE = {
        index: 'index',
        strategy: 'strategy',
        pinned : 'pinned'
    }

    constructor() {
        // 초기값
        this.current = this.SUBPANE_MODE.index
    }

    initialize(){
        let self = this

        const matches = document.querySelectorAll('.cs-handle-items-subpane')
        matches.forEach(function (it) {
            it.addEventListener('click', function (e) {
                // console.log(e.target.dataset.target)
                const target = e.target.dataset.target
                self.changeSubPane(target)
            })
        })
    }

    /**
     * 서브 판의 교체
     * @param {string} mode 
     */
    changeSubPane(mode){
        const subpane_list = document.querySelectorAll("#pills-items > div")
        subpane_list.forEach(function (item) {
            item.style.display = 'none'
        })
        let target_id = ''
        
        if(mode == this.SUBPANE_MODE.index){
            target_id = 'subpane_asset_index'
        } else if(mode == this.SUBPANE_MODE.strategy){
            target_id = 'subpane_asset_strategy'
        } else if(mode == this.SUBPANE_MODE.pinned){
            target_id = 'subpane_asset_pinned'
        } else {
            return
        }
        this.current = mode

        // show 처리
        const target = document.getElementById(target_id)
        target.style.display = 'block'
    }
}

/**
 * 메인 탭과 판의 이동에 관한 핸들링하는 클래스.
 */
class MainPaneHandle {
    PANE_MODE = {
        year: 'choice-years',
        money: 'choice-money',
        risk: 'choice-risk',
        asset: 'choice-asset'
    }

    constructor() {
        // 초기값
        this.current = this.PANE_MODE.year
        this.assetSubPane = new AssetSubPaneHandle()
        this.assetSubPane.initialize()
    }

    // 이벤트 바인딩
    initialize() {
        let self = this

        // 탭에 바인딩
        var tabElements = document.querySelectorAll('a[data-bs-toggle="pill"]')
        // console.log(tabElements)
        tabElements.forEach(tabEl => {
            tabEl.addEventListener('shown.bs.tab', e => {
                this.onChangeEvent(e, self)
            })
        })

        // 최초 1회 실행시킬 거 필요...

        // 이전, 다음 버튼 이벤트 바인딩
        document.getElementById("handle_pane_prev").addEventListener('click', e => {
            this.onClickPrev(e, self)
        })
        document.getElementById("handle_pane_next").addEventListener('click', e => {
            this.onClickNext(e, self)
        })
    }

    // 판이 변경될 때 동작되는 함수
    onChangeEvent(e, self) {
        // event.target // newly activated tab
        // event.relatedTarget // previous active tab
        // console.log(e.target)
        // console.log(e.relatedTarget)
        const target_id = e.target.id
        // console.log(target_id)

        const btn_prev = document.getElementById('handle_pane_prev')
        const btn_next = document.getElementById('handle_pane_next')

        if (target_id == 'pills-years-tab') {
            self.current = this.PANE_MODE.year
            btn_prev.style.display = 'none'
            btn_next.style.display = 'inline-block'
        } else if (target_id == 'pills-money-tab') {
            self.current = this.PANE_MODE.money
            btn_prev.style.display = 'inline-block'
            btn_next.style.display = 'inline-block'
        } else if (target_id == 'pills-risk-tab') {
            self.current = this.PANE_MODE.risk
            btn_prev.style.display = 'inline-block'
            btn_next.style.display = 'inline-block'
        } else if (target_id == 'pills-items-tab') {
            self.current = this.PANE_MODE.asset
            btn_prev.style.display = 'inline-block'
            btn_next.style.display = 'none'
        }
    }

    /**
     * 이전 버튼 클릭 이벤트
     * @param {event} e 
     * @param {object} self 
     */
    onClickPrev(e, self) {
        if (self.current == this.PANE_MODE.year) {
            // 없음. 혹은 포트폴리오 선택 초기 화면으로 이동?
        } else if (self.current == this.PANE_MODE.money) {
            // 투자 기간으로 이동.
            self.changeTap(this.PANE_MODE.year)
        } else if (self.current == this.PANE_MODE.risk) {
            // 투자 금액으로 이동.
            self.changeTap(this.PANE_MODE.money)
        } else if (self.current == this.PANE_MODE.asset) {
            if(self.assetSubPane.current == self.assetSubPane.SUBPANE_MODE.index){
                if (!document.getElementById("pills-risk-tab")) {
                    // 투자 금액으로 이동
                    self.changeTap(this.PANE_MODE.money)
                } else {
                    // 감당 리스크로 이동
                    self.changeTap(this.PANE_MODE.risk)
                }
            } else {
                self.assetSubPane.changeSubPane(self.assetSubPane.SUBPANE_MODE.index)
            }
        }
    }

    /**
     * 다음 버튼 클릭 이벤트
     * @param {event} e 
     * @param {object} self 
     */
    onClickNext(e, self) {
        // console.log(e)
        if (self.current == this.PANE_MODE.year) {
            // 투자 금액으로 이동.
            self.changeTap(this.PANE_MODE.money)
        } else if (self.current == this.PANE_MODE.money) {
            if (!document.getElementById("pills-risk-tab")) {
                // 투자 종목으로 이동.
                self.changeTap(this.PANE_MODE.asset)
            } else {
                // 감당 리스크로 이동.
                self.changeTap(this.PANE_MODE.risk)
            }
        } else if (self.current == this.PANE_MODE.risk) {
            // 종목 선택으로 이동
            self.changeTap(this.PANE_MODE.asset)
        }
    }

    /**
     * 탭을 전환시키는 함수
     */
    changeTap(mainPane, subPane = '') {
        let tab_selector = ''
        if (mainPane == this.PANE_MODE.money) {
            tab_selector = '#pills-money-tab'
        } else if (mainPane == this.PANE_MODE.year) {
            tab_selector = '#pills-years-tab'
        } else if (mainPane == this.PANE_MODE.risk) {
            tab_selector = '#pills-risk-tab'
        } else if (mainPane == this.PANE_MODE.asset) {
            tab_selector = '#pills-items-tab'
        }

        // 탭 전환
        this.changeBootstrapTab(tab_selector)
    }

    /**
     * 부트스트랩의 탭 변경 기능
     */
    changeBootstrapTab(tab_selector) {
        if (tab_selector != '') {
            var triggerEl = document.querySelector(tab_selector)
            // var tab = new bootstrap.Tab(triggerEl)
            var tab = bootstrap.Tab.getOrCreateInstance(triggerEl) // Returns a Bootstrap tab instance
            tab.show()
        }
    }
}
const mainPaneHandle = new MainPaneHandle()
mainPaneHandle.initialize()


/*
const assets_subpane_handles = document.querySelectorAll('.cs-handle-items-subpane')
assets_subpane_handles.forEach(function (it) {
    it.addEventListener('click', function (e) {
        handleChoiceAssetSubPane(this)
    })
})

function handleChoiceAssetSubPane(el) {
    const subpane_list = document.querySelectorAll("#pills-items > div")
    subpane_list.forEach(function (item) {
        item.style.display = 'none'
    })
    const target = document.querySelector(el.dataset.target)
    target.style.display = 'block'
    if (el.dataset.target == '#pane-pinned-items') {
        is_custom_asset = true
    } else {
        is_custom_asset = false
    }
}
*/


// const assetSubPaneHandle = new AssetSubPaneHandle()
// assetSubPaneHandle.initialize()

/*
document.addEventListener('click', function(e){

})
function aaaa(){
  var matches = document.querySelectorAll("#pills-items > div")
  matches.forEach(function(item) {
    item.style.display = 'none'
  });
  console.log(this.target)
  var el = document.querySelector('#pane-strategy-items')
  el.style.display = 'block'
}
*/
// validation
const form = document.getElementsByTagName('form')[0];
form.onkeypress = function(e) {
    var key = e.charCode || e.keyCode || 0;     
    if (key == 13) {
        e.preventDefault();
    }
}

class FormSubmit {
    constructor(){
        this.assetType = 'custom'
        this.isDebug = true
    }
    initialize(){
        var buttons = document.querySelectorAll("button[type=submit]");
        buttons.forEach(el => {
            el.addEventListener('click', e => {
                e.preventDefault()

                const btn = e.target
                // console.log('zzz')
                this.spinner(btn)
                if (btn.dataset.assetType == 'custom'){
                    return this.onSubmit('custom')
                } else {
                    return this.onSubmit('strategy')
                }
            })
        })
    }
    spinner(btn){
        // console.log(btn)
        btn.innerHTML = `
            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
            Loading...
        `
        btn.setAttribute('disabled', true)
    }
    validate(){
        this.debug('validate start')

        // 최적화 기법 종류
        // const optimize_method = document.getElementById("p_optimize_method").value
        // const optimize_method = document.getElementsByName("optimize_method")[0].value
        const optimize_method = this.getValueByName('optimize_method')

        // 감당 리스크 체크. (max sharpe 일 때는 제외)
        // 최소 리스크 값이 있는 듯.
        if (optimize_method != 'max_sharpe') {
            // 
            const risk = this.parseFloat(this.getValueByName('risk'))
            if(risk < 0.3){
                return this.validFailed('감당 리스크 수치가 적음')
            }
        }

        // 종목 선택 관련
        const asset_method_el = document.getElementsByName("asset_method")[0]
        if (this.assetType == 'custom') {
            // 관심 종목에서 선택
            asset_method_el.value = 'custom'
        } else {
            // 전략별 종목 선택시
            // const v = Array.from(document.getElementsByName("option_asset_method")).find(r => r.checked).value
            const v = this.getValueByName('option_asset_method')
            asset_method_el.value = v
        }

        // 금액 체크
        // const money = this.parseInt(document.getElementById('idMoney').value)
        const money = this.parseInt(this.getValueByName('money'))
        // this.debug(money)
        if (money <= 10000) {
            return this.validFailed('금액이 부족함')
        }

        // 이상 없으므로 submit 진행
        return true
    }
    onSubmit(assetType){
        this.assetType = assetType

        if(this.validate()){
            const form = document.getElementsByTagName('form')[0]
            form.submit()
        }
    }
    validFailed(msg) {
        console.log(msg)
        return false
    }
    getValueByName(name){
        const firstEl = document.getElementsByName(name)[0]
        const type = firstEl.type
        if(type == 'radio'){
            return Array.from(document.getElementsByName(name)).find(r => r.checked).value
        } else {
            return firstEl.value
        }
    }
    parseInt(v){
        return parseInt(v) || 0
    }
    parseFloat(v){
        return parseFloat(v) || 0.0
    }
    debug(msg){
        if(this.debug){
            console.log(msg)
        }
    }
}
var ss = new FormSubmit()
ss.initialize()



/*
form.addEventListener('submit', function (e) {
    return onSubmit(e)

    function onSubmit(e) {
        // console.log(e)

        e.preventDefault()

        // 최적화 기법 종류
        const optimize_method = document.getElementById("p_optimize_method").value

        // 감당 리스크 체크. (max sharpe 일 때는 제외)
        // 최소 리스크 값이 있는 듯.
        if (optimize_method != 'max_sharpe') {
        }

        // 금액 체크
        const money = parseInt(document.getElementById('idMoney').value)
        if (money <= 10000) {
            return validFailed('금액이 부족함')
        }

        // 종목 선택 관련
        const asset_method_el = document.getElementsByName("asset_method")[0]
        console.log(e)
        if (e.dataset.assetType=='custom') {
            asset_method_el.value = 'custom'
        } else {
            const v = Array.from(document.getElementsByName("option_asset_method")).find(r => r.checked).value
            asset_method_el.value = v
        }

        // 이상 없으므로 submit 진행
        return false
        // return true
    }

    function validFailed(msg) {
        return false
    }
})
*/
// console.log(document.getElementsByName("year"))
// console.log(document.getElementsByName("money")[0].type)