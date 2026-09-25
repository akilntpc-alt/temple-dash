import sys
h = open('index.html', encoding='utf-8').read()
old = ").insert({ user_id: tdUserId, event_type: 'game_over', score: sc, coins: co }).then(function () {});\n    sb.from('players').select('games_played').eq('id', tdUserId).then(function (r) {\n      var gp = (r.data && r.data[0] && Number(r.data[0].games_played)) || 0;\n      return sb.from('players').update({ games_played: gp + 1 });\n    }).then(function () { return pushStats(); }).catch(function () {});"
new = ").insert({ user_id: tdUserId, event_type: 'game_over', score: sc, coins: co }).then(function () {});\n    sb.from('players').select('games_played,total_coins').eq('id', tdUserId).then(function (r) {\n      var gp = (r.data && r.data[0] && Number(r.data[0].games_played)) || 0;\n      var tc = (r.data && r.data[0] && Number(r.data[0].total_coins)) || 0;\n      return sb.from('players').update({ games_played: gp + 1, total_coins: tc + co });\n    }).then(function () { return pushStats(); }).catch(function () {});"
if old in h:
    h = h.replace(old, new)
    open('index.html', 'w', encoding='utf-8').write(h)
    print('coins patch applied')
elif new in h:
    print('coins patch already applied')
else:
    print('PATCH TARGET NOT FOUND'); sys.exit(1)
