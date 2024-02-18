#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  const revList = [];

  for (let i = 0, j = 0; len >= i; len--, j++) {
    revList[j] = list[len];
  }
  return revList;
};
