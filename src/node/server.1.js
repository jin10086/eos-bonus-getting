var express = require('express')
// var BigInt = require("big-integer");


M = ["VsO/SgvCoVXDiw==", "wr/DlcOgS8OtYg==", "SA1Yw4XDnw==", "R3LDmMOFJgg3", "HyFzA8KcOQ5rAsOsaHfDhMKEw6NAXH1xwq/DoMKIwoksJMOMw6g=", "w68bw4rCv8Kawq7CiMKkXjY=", "VBUT"];
! function (t, e) {
    ! function (e) {
        for (; --e;) t.push(t.shift())
    }(++e)
}(M, 278);
var z = function t(e, n) {
    var o = M[e -= 0];
    if (void 0 === t.nULQIX) {
        ! function () {
            var t = function () {
                var t;
                try {
                    t = Function('return (function() {}.constructor("return this")( ));')()
                } catch (e) {
                    t = window
                }
                return t
            }();
            t.atob || (t.atob = function (t) {
                for (var e, n, o = String(t).replace(/=+$/, ""), a = 0, i = 0, r = ""; n = o.charAt(i++); ~n && (e = a % 4 ? 64 * e + n : n, a++ % 4) ? r += String.fromCharCode(255 & e >> (-2 * a & 6)) : 0) n = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".indexOf(n);
                return r
            })
        }();
        t.UVcWxp = function (t, e) {
            for (var n, o = [], a = 0, i = "", r = "", s = 0, c = (t = atob(t)).length; s < c; s++) r += "%" + ("00" + t.charCodeAt(s).toString(16)).slice(-2);
            t = decodeURIComponent(r);
            for (var l = 0; l < 256; l++) o[l] = l;
            for (l = 0; l < 256; l++) a = (a + o[l] + e.charCodeAt(l % e.length)) % 256, n = o[l], o[l] = o[a], o[a] = n;
            l = 0, a = 0;
            for (var d = 0; d < t.length; d++) a = (a + o[l = (l + 1) % 256]) % 256, n = o[l], o[l] = o[a], o[a] = n, i += String.fromCharCode(t.charCodeAt(d) ^ o[(o[l] + o[a]) % 256]);
            return i
        }, t.jEjHbw = {}, t.nULQIX = !0
    }
    var a = t.jEjHbw[e];
    return void 0 === a ? (void 0 === t.ReuwHb && (t.ReuwHb = !0), o = t.UVcWxp(o, n), t.jEjHbw[e] = o) : o = a, o
};

function D(t) {
    return t[z("0x0", "0e8D")](0)
}

function I(t) {
    for (var e = 0, n = 0; n < t.length; n++) e += D(t[n]);
    return e
}

function run(name, blocknum) {
    for (
        o = I(name),
        a = blocknum,
        i = BigInt(o) + BigInt(a),
        console.log(o),
        r = BigInt(1),
        s = BigInt(0); s < BigInt(7069); s++) {
        r *= i, r %= BigInt(7387)
    }
    return parseInt(r);

}
var app = express()

app.set('port', (process.env.PORT || 5000))

app.get('/betdice', function (req, res) {
    let name = req.query.name;
    let blocknum = req.query.blocknum;
    let r = run(name, parseInt(blocknum))
    res.send({
        "b": blocknum,
        "c": r
    })
})

app.listen(app.get('port'), function () {
    console.log("Node app is running at localhost:" + app.get('port'))
})