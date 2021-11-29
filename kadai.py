# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 16:57:44 2021

@author: nonno
"""

import streamlit as st


def main():
    st.title("家でもできるトレーニングメニュー")
    block_list = ["初級", "中級", "上級"]
    control_features = st.sidebar.selectbox("レベルを選択してください", block_list)
    st.header(f"{control_features}トレーニング")
    if control_features == "初級":
        visualize1(1)
    elif control_features == "中級":
        visualize2(2)
    elif control_features == "上級":
        visualize3(3)

from time import sleep   
def visualize1(file):
    if st.sidebar.checkbox("全身トレーニング"):
        st.subheader("～全身トレーニング～ 3~4分　19kcal")
        
        st.subheader("(1/5)ジャンピングジャック 15秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=2W4ZNSwoW_4")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=2W4ZNSwoW_4")
        if st.button("タイマースタート",1):
            target_time = 15
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",25):
                st.stop()
            down_timer(target_time)
            
        st.subheader("(2/5)Vクランチ 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=AkHgaJiwtFE")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=AkHgaJiwtFE")
            
        st.subheader("(3/5)プッシュアップ 3回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=eMQuAjuPCV0")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=eMQuAjuPCV0")
            
        st.subheader("(4/5)ランジツイスト 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=JSRQ595yY2U")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=JSRQ595yY2U")
            
        st.subheader("(5/5)プランク 25秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Fcbw82ykBvY")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Fcbw82ykBvY")
        if st.button("タイマースタート",2):
            target_time = 25
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",26):
                st.stop()
            down_timer(target_time)
            
        if st.button("初級　全身トレーニング完了！",16):
            st.title("お疲れ様でした！")
            st.balloons()
        
    if st.sidebar.checkbox("腹筋トレーニング"):
        st.subheader("～腹筋トレーニング～ 2~4分　19kcal")
        
        st.subheader("(1/4)アブドミナル・クランチ 8回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=RUNrHkbP4Pc")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=RUNrHkbP4Pc")
            
        st.subheader("(2/4)シットアップ 14回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=swOyWKk7Oko")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=swOyWKk7Oko")
            
        st.subheader("(3/4)レッグレイズ 6回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=dGKbTKLnym4")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=dGKbTKLnym4")
            
        st.subheader("(4/4)プランク 30秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Fcbw82ykBvY")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Fcbw82ykBvY")
        if st.button("タイマースタート",3):
            target_time = 30
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",27):
                st.stop()
            down_timer(target_time)
            
        if st.button("初級　腹筋トレーニング完了！",17):
            st.title("お疲れ様でした！")
            st.balloons()

    if st.sidebar.checkbox("ヒップアップトレーニング"):
        st.subheader("～ヒップアップトレーニング～ 4~7分　33kcal")
        
        st.subheader("(1/6)スタンディング・グルート・キックバック 16回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=x38_i24TBKo")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=x38_i24TBKo")
            
        st.subheader("(2/6)スクワット 15回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=YD5OhmTxGAw")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=YD5OhmTxGAw")
            
        st.subheader("(3/6)右ドンキーキック 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Sc8e7yCYvPQ")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Sc8e7yCYvPQ")
            
        st.subheader("(4/6)左ドンキーキック 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Sc8e7yCYvPQ")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Sc8e7yCYvPQ")
            
        st.subheader("(5/6)ヒップ・ブリッジ 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=9qo48CYN06w")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=9qo48CYN06w")
            
        st.subheader("(6/6)空気イス 10秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=zoBEgkd78Wg")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=zoBEgkd78Wg")
        if st.button("タイマースタート",4):
            target_time = 10
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",28):
                st.stop()
            down_timer(target_time)
            
        if st.button("初級　ヒップアップトレーニング完了！",18):
            st.title("お疲れ様でした！")
            st.balloons()
        
def visualize2(file):
    if st.sidebar.checkbox("全身トレーニング"):
        st.subheader("～全身トレーニング～ 7~10分　48kcal")
        
        st.subheader("(1/9)ジャンピングジャック 15秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=2W4ZNSwoW_4")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=2W4ZNSwoW_4")
        if st.button("タイマースタート",5):
            target_time = 15
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",29):
                st.stop()
            down_timer(target_time)
            
        st.subheader("(2/9) プッシュアップ 5回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=eMQuAjuPCV0")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=eMQuAjuPCV0")
            
        st.subheader("(3/9)スーパーマン 15回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=pGeaBXLwDtw")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=pGeaBXLwDtw")
            
        st.subheader("(4/9)カーツィーランジ 15回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=ekQQ70ZJjCE")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=ekQQ70ZJjCE")
            
        st.subheader("(5/9)クロスアーム・クランチ 15回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Qz3ylqqJ90M")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Qz3ylqqJ90M")
            
        st.subheader("(6/9)膝つきプッシュアップ 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=KFxW5amBbsw")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=KFxW5amBbsw")
            
        st.subheader("(7/9)左サイドプランク 20秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=2W96p2PIoPg")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=2W96p2PIoPg")
        if st.button("タイマースタート",6):
            target_time = 20
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",30):
                st.stop()
            down_timer(target_time)
            
        st.subheader("(8/9)アップ＆ダウンプランク 15回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=BZYnP1DXOdE")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=BZYnP1DXOdE")
            
        st.subheader("(9/9)右サイドプランク 20秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=2W96p2PIoPg")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=2W96p2PIoPg")
        if st.button("タイマースタート",7):
            target_time = 20
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",31):
                st.stop()
            down_timer(target_time)
            
        if st.button("中級　全身トレーニング完了！",19):
            st.title("お疲れ様でした！")
            st.balloons()

    if st.sidebar.checkbox("腹筋トレーニング"):
        st.subheader("～腹筋トレーニング～ 5~8分　51kcal")
        
        st.subheader("(1/4)アブドミナル・クランチ 30回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=RUNrHkbP4Pc")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=RUNrHkbP4Pc")
            
        st.subheader("(2/4)リバース・クランチ 30回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=UwRfRN5fYRg")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=UwRfRN5fYRg")
            
        st.subheader("(3/4)クロスアーム・クランチ 30回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Qz3ylqqJ90M")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Qz3ylqqJ90M")
            
        st.subheader("(4/4)プランク 30秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Fcbw82ykBvY")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Fcbw82ykBvY")
        if st.button("タイマースタート",8):
            target_time = 30
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",32):
                st.stop()
            down_timer(target_time)
            
        if st.button("中級　腹筋トレーニング完了！",20):
            st.title("お疲れ様でした！")
            st.balloons()

    if st.sidebar.checkbox("ヒップアップトレーニング"):
        st.subheader("～ヒップアップトレーニング～ 5~7分　40kcal")
        
        st.subheader("(1/6)スクワット 20回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=YD5OhmTxGAw")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=YD5OhmTxGAw")
            
        st.subheader("(2/6)マウンテン・クライマー 20回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=wQq3ybaLZeA")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=wQq3ybaLZeA")
            
        st.subheader("(3/6)右ファイヤー・ハイドラント 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=5u6klvw1oh0")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=5u6klvw1oh0")
            
        st.subheader("(4/6)左ファイヤー・ハイドラント 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=5u6klvw1oh0")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=5u6klvw1oh0")
            
        st.subheader("(5/6)ヒップ・ブリッジ 15回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=9qo48CYN06w")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=9qo48CYN06w")
            
        st.subheader("(6/6)サイド・ホップ 10秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=wcQqb9hVS_Y")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=wcQqb9hVS_Y")
        if st.button("タイマースタート",9):
            target_time = 10
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",33):
                st.stop()
            down_timer(target_time)
            
        if st.button("中級　ヒップアップトレーニング完了！",21):
            st.title("お疲れ様でした！")
            st.balloons()
    
def visualize3(file):
    if st.sidebar.checkbox("全身トレーニング"):
        st.subheader("～全身トレーニング～　10~16分　80kcal")
        
        st.subheader("(1/13)膝つきプッシュアップ 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=KFxW5amBbsw")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=KFxW5amBbsw")
            
        st.subheader("(2/13)クロスアーム・クランチ 20回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Qz3ylqqJ90M")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Qz3ylqqJ90M")
            
        st.subheader("(3/13)プッシュアップ 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=eMQuAjuPCV0")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=eMQuAjuPCV0")
            
        st.subheader("(4/13)ジャンピング・スクワット 20回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=xXLRbLdmwo8")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=xXLRbLdmwo8")
            
        st.subheader("(5/13)サイドランジ 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=iAV9ic-ed3w")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=iAV9ic-ed3w")
            
        st.subheader("(6/13)回転付きプッシュアップ 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=NTwhw_HxxdA")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=NTwhw_HxxdA")
            
        st.subheader("(7/13)サイドランジ 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=iAV9ic-ed3w")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=iAV9ic-ed3w")
            
        st.subheader("(8/13)プランク 60秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Fcbw82ykBvY")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Fcbw82ykBvY")
        if st.button("タイマースタート",10):
            target_time = 60
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",34):
                st.stop()
            down_timer(target_time)
            
        st.subheader("(9/13)右バックワードランジ・フロントキック 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=6Y95oA0RpgU")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=6Y95oA0RpgU")
            
        st.subheader("(10/13)左バックワードランジ・フロントキック 10回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=6Y95oA0RpgU")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=6Y95oA0RpgU")
            
        st.subheader("(11/13)ハイニ― 25秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Cmxr9xcNhgU")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Cmxr9xcNhgU")
        if st.button("タイマースタート",11):
            target_time = 25
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",35):
                st.stop()
            down_timer(target_time)
            
        st.subheader("(12/13)プランク 30秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Fcbw82ykBvY")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Fcbw82ykBvY")
        if st.button("タイマースタート",12):
            target_time = 30
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",36):
                st.stop()
            down_timer(target_time)
            
        st.subheader("(13/13)ブリッジ 30秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=A9J-1LHgnSw")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=A9J-1LHgnSw")
        if st.button("タイマースタート",13):
            target_time = 30
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",37):
                st.stop()
            down_timer(target_time)
            
        if st.button("上級　全身トレーニング完了！",22):
            st.title("お疲れ様でした！")
            st.balloons()
            
    if st.sidebar.checkbox("腹筋トレーニング"):
        st.subheader("～腹筋トレーニング～　7~10分　73kcal")
        
        st.subheader("(1/4)アブドミナル・クランチ 40回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=RUNrHkbP4Pc")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=RUNrHkbP4Pc")
            
        st.subheader("(2/4)ロングアーム・クランチ 40回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=GxKoSEkmRC8")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=GxKoSEkmRC8")
            
        st.subheader("(3/4)ロシアン・ツイスト 50回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=DJQGX2J4IVw")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=DJQGX2J4IVw")
            
        st.subheader("(4/4)プランク 40秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Fcbw82ykBvY")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Fcbw82ykBvY")
        if st.button("タイマースタート",14):
            target_time = 40
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",38):
                st.stop()
            down_timer(target_time)
            
        if st.button("上級　腹筋トレーニング完了！",23):
            st.title("お疲れ様でした！")
            st.balloons()
            
    if st.sidebar.checkbox("ヒップアップトレーニング"):
        st.subheader("～ヒップアップトレーニング～ 8~12分　85kcal")
        
        st.subheader("(1/5)スクワット 40回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=YD5OhmTxGAw")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=YD5OhmTxGAw")
            
        st.subheader("(2/5)大臀筋フロッグ・リフト 40回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=FLvOCG1a2a4")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=FLvOCG1a2a4")
            
        st.subheader("(3/5)プリエ・スクワット 40回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=Y8Mk-oGDLAw")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=Y8Mk-oGDLAw")
            
        st.subheader("(4/5)ヒップ・ブリッジ 40回")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=9qo48CYN06w")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=9qo48CYN06w")
            
        st.subheader("(5/5)空気イス 20秒")
        with st.expander("やり方を見る"):
            st.video("https://www.youtube.com/watch?v=zoBEgkd78Wg")
            st.caption("引用：Leap Fitness　https://www.youtube.com/watch?v=zoBEgkd78Wg")
        if st.button("タイマースタート",15):
            target_time = 15
            def down_timer(secs):
                t=st.empty()
                for i in range(secs, -1, -1):
                    t.text(f"{i}")
                    sleep(1)
                    
                    if i == 0:
                        t.text("時間です！")
            if st.button("タイマー中止",39):
                st.stop()
            down_timer(target_time)
            
          
        if st.button("上級　ヒップアップトレーニング完了！",24):
            st.title("お疲れ様でした！")
            st.balloons()



if __name__ == "__main__":
    main()