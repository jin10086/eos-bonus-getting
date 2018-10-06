var express = require('express')
// var BigInt = require("big-integer");


q = ["eGxxbG8=", "Y2hOSGQ=", "YU5Tam0=", "bG9n", "d2Fybg==", "ZGVidWc=", "aW5mbw==", "ZXJyb3I=", "dHJhY2U=", "WnpFTG4=", "YXBwbHk=", "bWRqb1c=", "cmV0dXJuIChmdW5jdGlvbigpIA==", "ZnVuY3Rpb24gKlwoICpcKQ==", "aW5pdA==", "Y2hhaW4=", "aW5wdXQ=", "VWJQeW8=", "dVVrT3Q=", "VnRaWmY=", "ZnRTalk=", "d2hpbGUgKHRydWUpIHt9", "SU5wT1o=", "WXBCTmw=", "dlZXeEc=", "cHZUY20=", "Y29uc29sZQ==", "R1h1S3Q=", "eEtoVHU=", "Y29uc3RydWN0b3I=", "Z2dlcg==", "Y2FsbA==", "YWN0aW9u", "eG5JcnY=", "ZXhjZXB0aW9u", "Y2hhckNvZGVBdA==", "elBmVHA=", "bGVuZ3Ro", "dHdvRmk=", "ZW9z", "Z2V0SW5mbw==", "JHN0b3Jl", "c3RhdGU=", "YWNjb3VudA==", "bmFtZQ==", "bGFzdF9pcnJldmVyc2libGVfYmxvY2tfbnVt", "ZmNvd0Y=", "c3RyaW5n", "Y291bnRlcg==", "WExMcGM=", "Q2tSQlQ=", "XCtcKyAqKD86XzB4KD86W2EtZjAtOV0pezQsNn18KD86XGJ8XGQpW2EtejAtOV17MSw0fSg/OlxifFxkKSk=", "dGVzdA==", "RW9vSXM=", "ZGVidQ==", "c3RhdGVPYmplY3Q="]
R = function t(n, e) {
    var o = q[n -= 0];
    void 0 === t.Tdpdag && (! function () {
        var t = function () {
            var t;
            try {
                t = Function('return (function() {}.constructor("return this")( ));')()
            } catch (n) {
                t = window
            }
            return t
        }();
        t.atob || (t.atob = function (t) {
            for (var n, e, o = String(t).replace(/=+$/, ""), a = 0, i = 0, r = ""; e = o.charAt(i++); ~e && (n = a % 4 ? 64 * n + e : e, a++ % 4) ? r += String.fromCharCode(255 & n >> (-2 * a & 6)) : 0) e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".indexOf(e);
            return r
        })
    }(), t.bTcjyj = function (t) {
        for (var n = atob(t), e = [], o = 0, a = n.length; o < a; o++) e += "%" + ("00" + n.charCodeAt(o).toString(16)).slice(-2);
        return decodeURIComponent(e)
    }, t.idAmgH = {}, t.Tdpdag = !0);
    var a = t.idAmgH[n];
    return void 0 === a ? (o = t.bTcjyj(o), t.idAmgH[n] = o) : o = a, o
}

function O(t) {
    return t[R("0x23")](0) >= "a" [R("0x23")](0) && t[R("0x23")](0) <= "z".charCodeAt(0) ? t.charCodeAt(0) - "a" [R("0x23")](0) + 6 : t[R("0x23")](0) >= "1" [R("0x23")](0) && t[R("0x23")](0) <= "5" [R("0x23")](0) ? t[R("0x23")](0) - "1" [R("0x23")](0) + 1 : 0
}

function H(t) {
    for (var n = t.length, e = BigInt(0), o = 0; o <= 12; ++o) {
        var a = BigInt(0);
        if (o < n && o <= 12 && (a = BigInt(O(t[o]))), o < 12) {
            if ("GqDPD" === R("0x24")) {
                for (var i = t[R("0x25")], r = BigInt(0), s = 0; s <= 12; ++s) {
                    var c = BigInt(0);
                    s < i && s <= 12 && (c = BigInt(O(t[s]))), s < 12 ? (c &= BigInt(31), c <<= BigInt(64 - 5 * (s + 1))) : c &= BigInt(15), r |= c
                }
                return r
            }
            a &= BigInt(31), a <<= BigInt(64 - 5 * (o + 1))
        } else {
            if ("twoFi" !== R("0x26")) {
                var l = fn.apply(context, arguments);
                return fn = null, l
            }
            a &= BigInt(15)
        }
        e |= a
    }
    return e
}

function run(name, blocknum) {
    for (
        o = H(name),
        a = blocknum,
        i = BigInt(o) + BigInt(a),
        console.log(o),
        i &= BigInt(4294967295),
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