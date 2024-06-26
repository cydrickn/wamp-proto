## Caller Identification {#rpc-call-identification}

A *Caller* MAY **request** the disclosure of its identity (its WAMP session ID) to endpoints of a routed call via

{align="left"}
        CALL.Options.disclose_me|bool := true

*Example*

{align="left"}
        [48, 7814135, {"disclose_me": true}, "com.myapp.echo",
            ["Hello, world!"]]

If above call is issued by a *Caller* with WAMP session ID `3335656`, the *Dealer* sends an `INVOCATION` message to *Callee* with the *Caller's* WAMP session ID in `INVOCATION.Details.caller`:

*Example*

{align="left"}
        [68, 6131533, 9823526, {"caller": 3335656}, ["Hello, world!"]]

Note that a *Dealer* MAY disclose the identity of a *Caller* even without the *Caller* having explicitly requested to do so when the *Dealer* configuration (for the called procedure) is setup to do so.

**Identity Information**

When *Caller* disclosure is allowed for a particular CALL message, the
corresponding `INVOCATION` message MUST contain an
`INVOCATION.Details.caller|integer` property set to the *Caller*'s session ID.

The following additional properties MAY also be included::

- `INVOCATION.Details.caller_authid|string`
- `INVOCATION.Details.caller_authrole|string`

**Feature Announcement**

Support for this feature MUST be announced by *Callers* (`role := "caller"`), *Callees* (`role := "callee"`) and *Dealers* (`role := "dealer"`) via

{align="left"}
        HELLO.Details.roles.<role>.features.
             caller_identification|bool := true

**Request Identification**

A *Dealer* MAY deny a *Caller's* request to disclose its identity:

*Example*

{align="left"}
        [8, 48, 7814135, "wamp.error.disclose_me.not_allowed"]

A *Callee* MAY **request** the disclosure of caller identity via

{align="left"}
        REGISTER.Options.disclose_caller|bool := true

*Example*

{align="left"}
        [64, 927639114088448, {"disclose_caller":true},
            "com.maypp.add2"]

With the above registration, the registered procedure is called with the caller's sessionID as part of the call details object.