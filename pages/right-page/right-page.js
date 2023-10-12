// pages/right-page/right-page.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    list:[],
    height: 0,
  },
  jumpPageCenter:function(){
    wx.redirectTo({
      url: '/pages/center-page/center-page'
    })
  },
  jumpPageLeft:function(){
    wx.redirectTo({
      url: '/pages/left-page/left-page'
    })
  },
  friend:function(e){
    var friend=!this.data.friend;
    this.setData({
      friend:friend
    })
  },
  
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    let screenHeight = wx.getSystemInfoSync().windowHeight;
    this.getDate();
    this.setData({
      height: screenHeight - 200,
    });
  },
  getDate(){
    wx.request({
      url:"http://127.0.0.1:8000/users_sorted_by_chouma/", 
      method: 'POST',
      data: {
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      
      success: (res) => {
        if(res.statusCode == 200) {
          console.log('用户信息已成功保存到后端');
          console.log(res)//请求成功后的res
          this.setData({
            list:res.data
          })
          console.log.list;
        } else {
          console.error('保存到后端失败:', res);
        }
      },
      fail: (error) => {
        console.error('请求失败:', error);
      }
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