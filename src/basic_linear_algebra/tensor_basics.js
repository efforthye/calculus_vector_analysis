// node src/basic_linear_algebra/tensor_basics.js
import * as tf from '@tensorflow/tfjs';

// 2x3 tensor
const tensorX = tf.tensor2d([[1, 2, 3], [2, 3, 4]]);

// tensor 전체 출력
console.log({tensor: tensorX});
tensorX.array().then(arr => console.log(arr));

// shape, rank 확인
console.log(tensorX.shape);  // 모양: [2, 3]
console.log(tensorX.rank);   // 차원: 2

// 행 개수 및 원소 확인
console.log(tensorX.shape[0]); // 행 개수: 2
tensorX.array().then(arr => console.log(arr[0][0])); // 1

// 개별 원소 접근
tensorX.array().then(arr => {
    console.log(arr[0][0]);  // 1
    console.log(arr[1][0]);  // 2
    console.log(arr[1][2]);  // 4
});