import Services from "@/services/Services";

// convertion functions
function extData2Internal(payload) {
  return {
    id: payload.device_id,
    enabled: payload.state.enabled
  }
}

function internal2ExtData(payload) {
  return {
    device_id: payload.id,
    type: "light",
    state: {
      enabled: payload.enabled
    }
  }
}

// initial state
const state = {
  units: []
}

// getters
const getters = {
  enabled: (state, getters, rootState) => (id) => {
    let unit = state.units.find(unit => unit.id == id)
    return unit.enabled
  }
}

// actions
const actions = {
  syncUnits({
    commit
  }, payload) {
    commit('clearStates')

    Services.getLights({
      place_id: payload.place_id
    }).then(
      response => {
        // console.log("Received response: ");
        // console.log(response.data)
        for (let unit of response.data) {
          commit('setState', extData2Internal(unit))
        }
      },
      error => {
        console.log("Failed to request lights")
        console.log(error)
      }
    )
  },

  setState({
    commit
  }, payload) {
    commit('setState', payload)
    this._vm.$socket.emit('set_state', internal2ExtData(payload));
  }
}

// mutations
const mutations = {
  clearStates: (state) => {
    state.units = [];
  },

  setState: (state, payload) => {
    console.log("Light " + payload.id + " is " + payload.enabled)
    let unit = state.units.find(unit => unit.id == payload.id)
    if (unit === undefined) {
      state.units.push({
        id: payload.id,
        enabled: payload.enabled
      })
    } else {
      unit.enabled = payload.enabled
    }
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
