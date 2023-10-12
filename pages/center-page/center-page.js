// pages/top-page/top-page.js
const app = getApp()
Page({
  /**
   * 页面的初始数据
   */
  data: {
    avatarUrl:"",
    nickName2:"",
    nickName1:"",
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    canIUseGetUserProfile: false,
    canIUseOpenData: wx.canIUse('open-data.type.userAvatarUrl') && wx.canIUse('open-data.type.userNickName'), // 如需尝试获取用户信息可改为false
    showDialog: false,
    money:1000,
    get:true,
    pipei:false,
    monCount2:1000,
    monCount1:1000,
    juCount:1,
    list:[],
    height:0,
  },
  jumpPageLeft:function(){
    wx.redirectTo({
      url: '/pages/left-page/left-page'
    })
  },

  jumpPageRight:function(){
    wx.redirectTo({
      url: '/pages/right-page/right-page'
    })
   
  },
  jumpPageDouble:function(){
    wx.redirectTo({
      url: '/pages/Dgame-page/Dgame-page'
    })
  },
  jumpPageRobort:function(){
    wx.redirectTo({
      url: '/pages/Rgame-page/Rgame-page'
    })
  },
  jumpPageWeb:function(e){
    var pipei=!this.data.pipei;
    this.setData({
      pipei:pipei
    })
  },
  jumpPageRule:function()
  {
    wx.redirectTo({
      url:'/pages/rule-page/rule-page'
    })
  },
  bindViewTap:function(){
    let screenHeight = wx.getSystemInfoSync().windowHeight;
    this.setData({
      showModal: true,
      height: screenHeight - 380,
    })
    wx.request({
            url: 'http://127.0.0.1:8000/jilu/', 
            method: 'POST',
            data: {
              nickname: this.data.nickName2,
            },
            header: {
              'content-type': 'application/json' // 默认值
            },
            success: (res) => {
              if(res.statusCode == 200) {
                console.log('用户信息已成功保存到后端');
                console.log(res.data)//请求成功后的res
                 var history=res.data.历史记录.split(",");
                 var time=res.data.时间.split(",");
                 console.log(history);
                 console.log(time);
                 var list=[];
                 for(var i=0;i<history.length-1;i++)
                 {
                   var victory=true;
                  var result=history[i].indexOf("赢了");
                  if(result==-1)
                  victory=false;
                  var i_list={"result":history[i],"time":time[i+1],"victory":victory}
                  list.push(i_list);
                 }
                 this.setData({
                   list:list
                 })
                 console.log(this.data.list)
              } else {
                console.error('保存到后端失败:', res);
              }
            },
            fail: (error) => {
              console.error('请求失败:', error);
            }
          })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    var avatarUrl=wx.getStorageSync('avatarUrl');
    var nickName2=wx.getStorageSync('nickName');
    console.log(avatarUrl);
    console.log(nickName2);
    this.setData({
      avatarUrl:avatarUrl,
      nickName2:nickName2
    })
    wx.request({
            url: 'http://127.0.0.1:8000/save_user_info/', 
            method: 'POST',
            data: {
              nickname: this.data.nickName2,
            },
            header: {
              'content-type': 'application/json' // 默认值
            },
            success: (res) => {
              console.log(this.data.nickName2,'111111');
              if(res.statusCode == 200) {
                console.log('用户信息已成功保存到后端');
                console.log(res)//请求成功后的res
                 this.setData({
                   money:res.data.chouma
                 })
              } else {
                console.error('保存到后端失败:', res);
              }
            },
            fail: (error) => {
              console.error('请求失败:', error);
            }
          })
  },

   /**
   * 弹出框蒙层截断touchmove事件
   */
  preventTouchMove: function () {
  },
  /**
   * 隐藏模态对话框
   */
  hideModal: function () {
    this.setData({
      showModal: false
    });
  },
  /**
   * 对话框取消按钮点击事件
   */
  onCancel: function () {
    this.hideModal();
  },
  inputChangeMoney:function(e){
    var ju=e.detail.value;
    this.setData({
      monCount2:ju,
    })
  },
  inputChangeJu:function(e){
    var ju=e.detail.value;
    this.setData({
      juCount:ju,
    })
  },
  pipei(){
    this.setData({
      get:false
    })
    wx.request({
            url: 'http://127.0.0.1:8000/pipeiduiixang/', 
            method: 'POST',
            data: {
              nickname: this.data.nickName2,//玩家二昵称
              monCount:this.data.monCount2,//玩家二筹码
              juCount:this.data.juCount//局数
            },
            header: {
              'content-type': 'application/json' // 默认值
            },
            success: (res) => {
              if(res.statusCode == 200) {
                console.log('用户信息已成功保存到后端');
                console.log(res,'111111')//请求成功后的res
                var monCount1=res.data.筹码;
                var nickName1=res.data.nickname;
                this.setData({
                  monCount1:monCount1,
                  nickName1:nickName1
                })
                this.jump()
              } else {
                console.error('保存到后端失败:', res);
              }
            },
            fail: (error) => {
              console.error('请求失败:', error);
            }
          })
  },
  jump(){
    this.setData({
      pipei:false,
      get:true
    })
    var nickName1=this.data.nickName1;
    var nickName2=this.data.nickName2;
    var monCount1=this.data.monCount1;
    var monCount2=this.data.monCount2;
    var monCount=this.data.money;
    var juCount=this.data.juCount;
    wx.setStorageSync('nickName1', nickName1);
    wx.setStorageSync('nickName2',nickName2);
    wx.setStorageSync('monCount1',monCount1);
    wx.setStorageSync('monCount2',monCount2);
    wx.setStorageSync('monCount',monCount);
    wx.setStorageSync('juCount',juCount);
    wx.navigateTo({
      url: '/pages/Wgame-page/Wgame-page'
    })
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})