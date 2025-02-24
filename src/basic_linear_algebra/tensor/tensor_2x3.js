// node src/basic_linear_algebra/tensor/tensor_2x3.js
import * as tf from '@tensorflow/tfjs';

// 2x3 tensor 정의
const tensor_x = tf.tensor2d([[1, 2, 3], [2, 3, 4]]);

// tensor 전체 출력
console.log({tensor: tensor_x});
tensor_x.array().then(arr => console.log(arr));

// shape, rank 확인
console.log(tensor_x.shape);  // 모양: [2, 3]
console.log(tensor_x.rank);   // 차원: 2

// 행 개수 및 원소 확인
console.log(tensor_x.shape[0]); // 행 개수: 2
tensor_x.array().then(arr => console.log(arr[0][0])); // 1

// 개별 원소 접근
tensor_x.array().then(arr => {
    console.log(arr[0][0]);  // 1
    console.log(arr[1][0]);  // 2
    console.log(arr[1][2]);  // 4
});