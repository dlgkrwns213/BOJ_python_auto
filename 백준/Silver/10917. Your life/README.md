# [Silver II] Your life - 10917 

[문제 링크](https://www.acmicpc.net/problem/10917) 

### 성능 요약

메모리: 75324 KB, 시간: 484 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색

### 제출 일자

2025년 7월 13일 17:16:00

### 문제 설명

<p>당신이 꿈을 이루는 과정 중에 일어날 수 있는 수많은 상황들의 관계를 그래프로 나타내어 보겠다. 많은 상황을 압축해서 N개의 상황이 일어날 수 있다고 하고 1번에서 N까지의 번호를 붙였다. 당신은 현재 1번 상황에 있다. 그리고 N번 상황은 당신이 이루고자 하는 유일한 꿈이다.</p>

<p>상황은 당신의 선택에 따라 변화할 수 있다. 당신이 선택할 수 있는 변화는 총 M개 있으며 x, y의 형태로 주어진다. 이는 당신이 상태 x에 있는 경우 상태 y로 가는 선택을 할 수 있다는 것을 의미하며, x < y임이 보장된다.</p>

<p>당신은 꿈을 이룰 수 있을까? 이룰 수 있다면 당신의 상황이 변화하는 횟수를 최소한으로 줄이면 몇 번 만에 꿈을 이룰 수 있을까?</p>

### 입력 

 <p>첫 번째 줄에는 두 개의 자연수 N, M(0 ≤ M ≤ 200,000)이 주어진다.</p>

<p>이후 M개의 줄에는 두 개의 자연수 x, y(1 ≤ x < y ≤ N)가 공백으로 구분되어 주어진다</p>

<p>1 ≤ N ≤ 100,000인 입력이 주어진다.</p>

### 출력 

 <p>당신이 꿈을 이룰 수 있다면 꿈을 이루기 위해 필요한 상황 변화 수의 최솟값을 출력하고, 이룰 수 없다면 -1을 출력한다.</p>

