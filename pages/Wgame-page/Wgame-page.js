// pages/Wgame-page/Wgame-page.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    juCount:1,
    beiCount:1,
    end:false,
    people:false,
    monCount:1000,
    monCount1:1000,
    monCount2:1000,
    ThatBei:1,
    ThatNBei:1,
    ThisBei:1,
    ThisNBei:1,
    ThatLun:3,
    ThisLun:3,
    ThisJu:1,
    ThatJu:1,
    Thatc:0,
    areaList:[0,1,2,3],
    Num1:[{'Inid':'',Select:false},{'Inid':'',Select:false},{'Inid':'',Select:false},{'Inid':'',Select:false},{'Inid':'',Select:false}],
    Num2:[{'Inid':'',Select:false},{'Inid':'',Select:false},{'Inid':'',Select:false},{'Inid':'',Select:false},{'Inid':'',Select:false}],
    randomNumbers1: {}, // That中存储随机数字的数组
    randomNumbers12: {},//This中存储随机数组数据
    x1:[],
    x2:[],
    ThisCount:5,
    ThatCount:5,
    grade1:0,
    grade2:0,
    showModal:true,
    Peo1grade:1,
    Peo2grade:2,
    grade:1,
    nickName1:'',
    nickName2:''
  },

  get:function(e){//三轮AI

    var Lun=3-this.data.ThatLun;
    wx.request({
      url:"http://127.0.0.1:8000/save_AI_info"+Lun+"/", 
      method: 'POST',
      data: {
        RobotTou:this.data.randomNumbers1
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      success: (res) => {
        if(res.statusCode == 200) {
          console.log('用户信息已成功保存到后端');
          console.log(res)//请求成功后的res
          var x1=Object.values(res.data);
          var length=Object.keys(res.data).length;
          this.setData({
            x1:x1,
            ThatCount:5-length
          })
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
    wx.redirectTo({
      url: '/pages/center-page/center-page',
    })
  },

  over:function(){//保存玩家的选定区
    console.log(this.data.x2,'1111');//选定区域
    console.log(this.data.beiCount,'11111');//总倍数
    console.log(this.data.monCount2,'11111');//筹码数
    wx.request({
      url:"http://127.0.0.1:8000/save_zaixian_info/", 
      method: 'POST',
      data: {
        play1_xuandingquyu:this.data.x1,//玩家1选定区
        play1_nickname:this.data.nickName1,//玩家1昵称
        play1_chouma:this.data.monCount1,//玩家1筹码
        play2_xuandingquyu :this.data.x2,//玩家2选定区
        play2_nickna:this.data.nickName2,
        play2_chouma:this.data.monCount2,
        zongbeilv:this.data.beiCount,//总倍数
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      
      success: (res) => {
        if(res.statusCode == 200) {
          console.log('用户信息已成功保存到后端');
          console.log(res)//请求成功后的res
          var nickName1=res.data.玩家1昵称;
          var nickName2=res.data.玩家2昵称;
          var Peo1grade=res.data.玩家1得分;
          var Peo2grade=res.data.玩家2得分;
          var monCount1=res.data.玩家1筹码;
          var monCount2=res.data.玩家2筹码;
          var grade=Math.abs(monCount2-this.data.monCount2);
          this.setData({
            Peo1grade: Peo1grade,
            Peo2grade:Peo2grade,
            monCount1:monCount1,
            monCount2:monCount2,
            grade:grade
          })
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
   * 对话框确认按钮点击事件
   */
  onConfirm: function () {
    this.hideModal();
  },


  start1(e) {
    let numbers1 =[];
    let numbers2=[];
    var ThatLun=this.data.ThatLun-1;
    var ThisLun=this.data.ThisLun-1;
    var ThatBei=this.data.ThisBei+this.data.ThisNBei;
    var ThisBei=this.data.ThisBei+this.data.ThisNBei;
    var ThatJu=this.data.ThatJu;
    var ThisJu=this.data.ThisJu;
    var ThatCount=this.data.ThatCount;
    var ThisCount=this.data.ThisCount;
    var x1=this.data.x1;
    var x2=this.data.x2;
    var Peo1=this.data.monCount1;
    var Peo2=this.data.monCount2;
    while (numbers1.length < this.data.ThatCount) {
      const num1 = Math.floor(Math.random() * 6) + 1;
        numbers1.push(num1);
      }
      while (numbers2.length < this.data.ThisCount) {
        const num2 = Math.floor(Math.random() * 6) + 1;
          numbers2.push(num2);
        }
      if(this.data.ThatLun==0){
        ThatJu=ThatJu-1;
        ThisJu=ThatJu;
        this.over();
        ThatLun=ThisLun=3;
        ThatCount=ThisCount=5;
        ThatBei=ThisBei=1;
        beiCount=1;
        x1=x2=[];
      }
      let monCount1=this.data. monCount1;
      let  monCount2=this.data.monCount2;
      if(monCount1<=0||monCount2<=0||ThatJu<0)
        {this.gameover();}
      var beiCount=2*ThisBei;
      //console.log(numbers1)
      //console.log(numbers2)
      this.setData({
        randomNumbers1:numbers1,
        randomNumbers2:numbers2,
        ThatLun:ThatLun,
        ThisLun:ThisLun,
        ThatJu:ThatJu,
        ThisJu:ThisJu,
        ThatBei:ThatBei,
        ThisBei:ThisBei,
        ThatCount:ThatCount,
        ThisCount:ThisCount,
        beiCount:beiCount,
        x1:x1,
        x2:x2,
        monCount1:Peo1,
        monCount2:Peo2,
        'Num1[0].Inid':numbers1[0],
        'Num1[0].Select':false,
        'Num2[0].Inid':numbers2[0],
        'Num2[0].Select':false,
        'Num1[1].Inid':numbers1[1],
        'Num1[1].Select':false,
        'Num2[1].Inid':numbers2[1],
        'Num2[1].Select':false,
        'Num1[2].Inid':numbers1[2],
        'Num1[2].Select':false,
        'Num2[2].Inid':numbers2[2],
        'Num2[2].Select':false,
        'Num1[3].Inid':numbers1[3],
        'Num1[3].Select':false,
        'Num2[3].Inid':numbers2[3],
        'Num2[3].Select':false,
        'Num1[4].Inid':numbers1[4],
        'Num1[4].Select':false,
        'Num2[4].Inid':numbers2[4],
        'Num2[4].Select':false,
      });
      if(ThatLun!=3)
      {this.get();}
    },
  
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad(options) {
      var nickName1=wx.getStorageSync('nickName1');
    var nickName2=wx.getStorageSync('nickName2')
    var monCount1=wx.getStorageSync('monCount1')
    var monCount2=wx.getStorageSync('monCount2')
    var monCount=wx.getStorageSync('monCount');
    var juCount=wx.getStorageSync('juCount');
    console.log(nickName1);
    console.log(nickName2);
    console.log(monCount1);
    console.log(monCount2);
    this.setData({
      monCount:monCount,
      monCount1:monCount1,
      monCount2:monCount2,
      nickName1:nickName1,
      nickName2:nickName2,
      juCount:juCount,
      ThatJu:juCount-1,
      ThisJu:juCount-1,
    })
    },

    choosed1(e){
      let choosetTab = e.currentTarget.dataset.index;
      let chooset=e.currentTarget.dataset.id;
      let x1=this.data.x1;
      let inSelect=this.data.Num1[chooset].Select;
      let count=this.data.ThatCount;
      console.log(choosetTab);
      if(this.data.x1.length>4&&this.data.ThatLun==0){
        x1=[]
      }
      else if(inSelect==false)
      {
        x1=this.data.x1.concat(choosetTab);
        this.data.Num1[chooset].Select=true;
        this.data.ThatCount=count-1;
      };
      this.setData({
        x1:x1,
        Num1:this.data.Num1,
        ThatCount:this.data.ThatCount
      });
      console.log(this.data.Num1);
      console.log(this.data.ThatCount)
      console.log(x1)
    },
    choosed2(e){
      let choosetTab = e.currentTarget.dataset.index;
      let chooset=e.currentTarget.dataset.id;
      let x2=this.data.x2;
      let inSelect=this.data.Num2[chooset].Select;
      let count=this.data.ThisCount;
      console.log(choosetTab);
      if(this.data.x2.length>4&&this.data.ThisLun==0){
        x2=[]
      }
      else if(inSelect==false)
      {
        x2=this.data.x2.concat(choosetTab);
        this.data.Num2[chooset].Select=true;
        this.data.ThisCount=count-1;
      };
      this.setData({
        x2:x2,
        Num2:this.data.Num2,
        ThisCount:this.data.ThisCount
      });
      console.log(this.data.Num2);
      console.log(this.data.ThisCount)
      console.log(x2)
    },

  SgetValueTap(e){
    // console.log(e)
    // console.log(e.currentTarget.dataset.dialogid)
    let dialogid=e.currentTarget.dataset.dialogid;
    // console.log(this.data.areaList[dialogid])//得到倍率
    this.setData({
      ThisNBei:this.data.areaList[dialogid],//赋值给输入框
      Sindexstatus: dialogid, //更新
    })
  },
  AgetValueTap(e){
    // console.log(e)
    // console.log(e.currentTarget.dataset.dialogid)
    let dialogid=e.currentTarget.dataset.dialogid;
    // console.log(this.data.areaList[dialogid])
    this.setData({
      ThatNBei:this.data.areaList[dialogid],//赋值给输入框
      Aindexstatus: dialogid, //更新
    })
  },
  inputChangeMoney:function(e){
    var ju=e.detail.value;
    this.setData({
      monCount1:ju,
      monCount2:ju
    })
  },
  inputChangeJu:function(e){
    var ju=e.detail.value;
    this.setData({
      juCount:ju,
      ThatJu:ju-1,
      ThisJu:ju-1
    })
  },
  gameover(){
    this.setData({
      end:true
    })
  },
    Jmpe(){
        wx.redirectTo({
          url: '/pages/center-page/center-page',
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