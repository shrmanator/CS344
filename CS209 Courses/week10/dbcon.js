mysql = require('mysql');
var pool = mysql.createPool({
  connectionLimit : 10,
  host            : 'classmysql.engr.oregonstate.edu',
  user            : 'cs290_shermado',
  password        : 'Dovisthecoolest1',
  database        : 'cs290_shermado'
});

module.exports.pool = pool;
//
//
// mysql = require('mysql');
// let pool = mysql.createPool({
//   connectionLimit : 10,
//   host            : 'mysql.engr.oregonstate.edu',
//   user            : 'shermado',
//   password        : 'Dovisthecoolest1',
//   database        : 'cs290_shermado'
// });
// module.exports.pool = pool;